# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, QueryDict
from .serializers import InputSerializer, FileSerializer
from .models import parseInput
import jc
from django.utils import timezone
from rest_framework.decorators import api_view
import os
from django.core.files.uploadedfile import TemporaryUploadedFile

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

@csrf_exempt
@api_view(['POST'])
def addParse(request):
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


