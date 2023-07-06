# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import InputSerializer, FileSerializer
from .models import parseInput
from .models import File
import jc
from django.utils import timezone
from rest_framework.decorators import api_view
import os
import json
from rest_framework.parsers import FileUploadParser
from rest_framework import serializers


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


"""
Julian J.
At the moment this method instantly parses any data given in a text file
given the filename, the jc command needed, and p_input.
To-do
1)remove need for p_input variable is not needed in current version.
2)This version is currently reading a file that is is the app's working directory,
this should be changed into an uploaded file.
3)The method above called instant parse is a misnomer in the sense that that's exactly what this method does.

Also url for this request is:
http://localhost:8000/api/submit/?=test
"""


@csrf_exempt
@api_view(['POST'])
def addParse(request):
    if request.method == 'POST':
        # Handle file upload
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            # Access the uploaded file content
            file_content = file_serializer.instance.file.read().decode('utf-8')
            # Perform any necessary processing on the file content
        else:
            return JsonResponse(file_serializer.errors, status=400)
        
        # Handle JSON data
        data = request.data
        data['ticket_number'] = parseInput.objects.count() + 1
        data['client_ip'] = request.META.get('REMOTE_ADDR')
        data['time_created'] = timezone.now()
        data['time_finished'] = timezone.now()
        command = data['parser']
        data['file_content'] = file_content
        print(file_content)
        data['p_output'] = str(jc.parse(command, file_content))
        
        
        serializer = InputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

