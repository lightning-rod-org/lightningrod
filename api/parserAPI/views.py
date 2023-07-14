# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, QueryDict
from .serializers import InputSerializer, FileSerializer, TicketSerializer, AdditionalFieldsSerializer
from .models import parseInput, Ticket, AdditionalFields
import jc
from django.utils import timezone
from rest_framework.decorators import api_view
import os
from django.core.files.uploadedfile import TemporaryUploadedFile
from background_task import background
import json



@csrf_exempt
@api_view(['Get'])
def instantParse(request):
    """
    List all task snippets
    """
    if request.method == 'GET':        
        # parse the incoming information
        data = JSONParser().parse(request)  # this error was getting thrown because of the url syntax, url should be
        # http://localhost:8000/api/instantParse/
        here = os.path.dirname(os.path.abspath(__file__))  # create file path directly to this directory
        filename = os.path.join(here, data['filename'])  # create a new file name using the absolute path from above
        file = open(filename, 'r')  # open file using combined attributes from above in read mode
        data['ticket_number'] = parseInput.objects.count() + 1
        data['client_ip'] = request.META.get('REMOTE_ADDR')
        data['time_created'] = timezone.now()
        text = file.read()  # read entire text file into one string
        command = data['parser']  # decide which jc parser should be used for the text file
        data['time_finished'] = timezone.now()
        data['p_output'] = jc.parse(command, text)  # parse the given data with jc using the provided command

        # instanciate with the serializer
        serializer = InputSerializer(data=data)
        # check if the information is okay
        if serializer.is_valid():
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

#@background()
def parseData(request, file_content, passed_ticket):
    additional_fields = AdditionalFields(ticket=passed_ticket, time_created=timezone.now(), time_finished=timezone.now())
    additional_fields.client_ip = request.META.get("REMOTE_ADDR")
    additional_fields.ticket.update_status("In Progress")
    additional_fields.time_finished = timezone.now()

    assert isinstance(file_content, str)
    try:
        additional_fields.p_output = jc.parse(additional_fields.ticket.parser, file_content)
    except:
        additional_fields.p_output = {"p_output": None}
    # Convert Data from query dictionary to dictionary.

    additional_fields.ticket.update_status("Completed")
    serializer = AdditionalFieldsSerializer(data=additional_fields.__dict__)
    if (serializer.is_valid()):
        additional_fields.save()
        return additional_fields
    return None

def get_status(ticket):
    return ticket.status

@csrf_exempt
@api_view(['GET','POST'])
def addParse(request):
    if request.method == 'GET':
        number = request.GET.get('ticket_number')  # Assuming the ticket number is passed as a query parameter

        try:
            ticket = Ticket.objects.get(ticket_number=number)
            if (get_status(ticket) == "Completed"):
                additional_fields = AdditionalFields.objects.get(ticket=ticket)
                response_data = {
                    'ticket_number': ticket.ticket_number,
                    'parser': ticket.parser,
                    'status': ticket.status,
                    'client_ip': additional_fields.client_ip,
                    'time_created': additional_fields.time_created,
                    'time_finished': additional_fields.time_finished,
                    'p_output': additional_fields.p_output
                }
                return JsonResponse(response_data, status=200)
            else:
                return JsonResponse({'status': 'In Progress'}, status=400)
        except (Ticket.DoesNotExist, AdditionalFields.DoesNotExist):
            return JsonResponse({'error': 'Ticket not found'}, status=404)
    elif request.method == 'POST':
        # Create a ticket number with the status starting.
        data = request.data
        ticket_number = Ticket.objects.count() + 1  # Get the next available ticket number
        new_ticket = Ticket(ticket_number=ticket_number, parser=data.get('parser'), status='Starting')

        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_obj: TemporaryUploadedFile = request.FILES['file']  # Assuming the file field is named 'file'
            file_content = file_obj.read().decode('utf-8')
        else:
            return JsonResponse(file_serializer.errors, status=400)

        ticket_serializer = TicketSerializer(data=new_ticket.__dict__)
        if ticket_serializer.is_valid():
            ticket_serializer.save()
            parseData(request, file_content, new_ticket)
            
            return JsonResponse(ticket_serializer.data, status=201)
        else:
            return JsonResponse(ticket_serializer.errors, status=400)
    
    '''
    if request.method == 'POST':
        # Handle file upload
        data = request.data
        file_serializer = FileSerializer(data=data)
        if file_serializer.is_valid():
            file_obj: TemporaryUploadedFile = request.FILES['file']  # Assuming the file field is named 'file'
            file_content = file_obj.read().decode('utf-8')
        else:
            return JsonResponse(file_serializer.errors, status=400)

        # Handle JSON data
        data["ticket_number"] = parseInput.objects.count() + 1
        data["client_ip"] = request.META.get('REMOTE_ADDR')
        data["time_created"] = timezone.now()
        data["time_finished"] = timezone.now()
        command = data["parser"]
        assert isinstance(file_content, str)
        try:
            data["p_output"] = jc.parse(command, file_content)
        except:
            data["p_output"] = None
        
        # Convert Data from query dictionary to dictionary.
        data = QueryDict.dict(data)

        serializer = InputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    '''

