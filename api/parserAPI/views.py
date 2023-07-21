# parsing data from the client
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import FileSerializer, TicketSerializer , FinalTicketSerializer
from .models import Ticket, FinalTicket
import jc
from django.utils import timezone
from rest_framework.decorators import api_view
from django.core.files.uploadedfile import TemporaryUploadedFile
import threading
import uuid


@csrf_exempt
@api_view(['GET'])
def instantParse(request):
    if request.method == 'GET':
        number = request.GET.get('ticket_number')  # Assuming the ticket number is passed as a query parameter

        # Get the ticket number, if it exists. 
        try:
            ticket = Ticket.objects.get(ticket_number=number)
            response_data = {
                'ticket_number': ticket.ticket_number,
                'status': ticket.status,
                'parser': ticket.parser
            }

            # If status complete, update with the rest of the fields.
            if ticket.status == "Completed":
                final_tick = FinalTicket.objects.get(ticket=ticket)
                response_data.update({
                    'client_ip': final_tick.client_ip,
                    'time_created': final_tick.time_created,
                    'time_finished': final_tick.time_finished,
                    'p_output': final_tick.p_output
                })
                return JsonResponse(response_data, status=200)
            else:
                response_data.update({
                    'status': ticket.status
                })
                return JsonResponse(response_data, status=200)
        # Error in finding ticket number.
        except (Ticket.DoesNotExist, final_tick.DoesNotExist):
            return JsonResponse({'error': 'Ticket not found'}, status=404)

# Helper function to parse the data for extra fields.
def parseData(request, file_content, passed_ticket):
    final_tick = FinalTicket(ticket=passed_ticket, time_created=timezone.now(),
                                         time_finished=timezone.now())
    final_tick.client_ip = request.META.get("REMOTE_ADDR")
    final_tick.ticket.update_status("In Progress")
    final_tick.parser = final_tick.ticket.parser
    assert isinstance(file_content, str)

    # Check to make sure it is a valid parser.

    final_tick.p_output = jc.parse(final_tick.ticket.parser, file_content)

    # Update the status to complete and time finished.
    final_tick.ticket.update_status("Completed")
    final_tick.time_finished = timezone.now()

    #final_tick = FinalTicket(ticket_number = passed_ticket.ticket_number, parser = passed_ticket.parser, client_ip = FinalTicket.client_ip, time_created = FinalTicket.time_created, time_finished = FinalTicket.time_finished, p_output = FinalTicket.p_output  )
#     final_tick = FinalTicket(
#     first_ticket=passed_ticket,
#     client_ip=FinalTicket.client_ip,
#     time_created=FinalTicket.time_created,
#     time_finished=FinalTicket.time_finished,
#     p_output=FinalTicket.p_output
# )

    
    # Saves the additional fields.
    serializer = FinalTicketSerializer(data=final_tick.__dict__)
    # serializer2 = FinalTicketSerializer(data=final_tick.__dict__)
    # if serializer2.is_valid():
    #     print("got it")
    #     final_tick.save()
    # else:
    #     print("wrong")
    #     print(serializer2.errors)
 
    if serializer.is_valid():
        print("Data saved!")
        FinalTicket.save()
    else:
        print("Not valid!")
        print(serializer.errors)



@csrf_exempt
@api_view(['POST'])
def addParse(request):
    if request.method == 'POST':
        data = request.data
        if not jc.parser_mod_list().__contains__(data.get('parser')):
            return JsonResponse({"Error": "Invalid Parser Type"}, status=400)
        ticket_number = uuid.uuid4()  # Get the next available ticket number

        # Create a ticket number with the status starting.
        new_ticket = Ticket(ticket_number=str(ticket_number), parser=data.get('parser'), status='Starting')

        # Checks for a file.
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_obj: TemporaryUploadedFile = request.FILES['file']  # Assuming the file field is named 'file'
            file_content = file_obj.read().decode('utf-8')
        else:
            return JsonResponse(file_serializer.errors, status=400)

        # Checks to make sure it is a valid ticket.
        ticket_serializer = TicketSerializer(data=new_ticket.__dict__)
        if ticket_serializer.is_valid():
            ticket_serializer.save()

            # Create a new thread for each request.
            thread = threading.Thread(target=parseData, args=(request, file_content, new_ticket), daemon=True)
            thread.start()

            return JsonResponse(ticket_serializer.data, status=201)
        else:
            return JsonResponse(ticket_serializer.errors, status=400)