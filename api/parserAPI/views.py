# parsing data from the client
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import FileSerializer, TicketSerializer, AdditionalFieldsSerializer
from .models import Ticket, AdditionalFields
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
                additional_fields = AdditionalFields.objects.get(ticket=ticket)
                response_data.update({
                    'client_ip': additional_fields.client_ip,
                    'time_created': additional_fields.time_created,
                    'time_finished': additional_fields.time_finished,
                    'p_output': additional_fields.p_output
                })
                return JsonResponse(response_data, status=200)
            else:
                response_data.update({
                    'status': ticket.status
                })
                return JsonResponse(response_data, status=200)
        # Error in finding ticket number.
        except (Ticket.DoesNotExist, AdditionalFields.DoesNotExist):
            return JsonResponse({'error': 'Ticket not found'}, status=404)


# Helper function to parse the data for extra fields.
def parseData(request, file_content, passed_ticket):
    additional_fields = AdditionalFields(ticket=passed_ticket, time_created=timezone.now(),
                                         time_finished=timezone.now())
    additional_fields.client_ip = request.META.get("REMOTE_ADDR")
    additional_fields.ticket.update_status("In Progress")

    assert isinstance(file_content, str)

    # Check to make sure it is a valid parser.

    additional_fields.p_output = jc.parse(additional_fields.ticket.parser, file_content)

    # Update the status to complete and time finished.
    additional_fields.ticket.update_status("Completed")
    additional_fields.time_finished = timezone.now()

    # Saves the additional fields.
    serializer = AdditionalFieldsSerializer(data=additional_fields.__dict__)
    if serializer.is_valid():
        print("Data saved!")
        additional_fields.save()
    else:
        print("Not valid!")


@csrf_exempt
@api_view(['POST'])
def addParse(request):
    if request.method == 'POST':
        data = request.data
        if not jc.parser_mod_list().__contains__(data.get('parser')):
            return JsonResponse({"Error": "Invalid Parser Type"}, status=400)
        ticket_number = str(uuid.uuid4())  # Get the next available ticket number

        # Create a ticket number with the status starting.
        new_ticket = Ticket(ticket_number=ticket_number, parser=data.get('parser'), status='Starting')

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

@csrf_exempt
@api_view(['GET'])
def getParsers(request):
    if request.method == 'GET':
        return JsonResponse({ "parsers": jc.standard_parser_mod_list()}, status=200)
