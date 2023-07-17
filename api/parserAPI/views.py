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
from django.http import HttpResponse
import asyncio
import httpx
from django.core.files.uploadedfile import TemporaryUploadedFile
from asgiref.sync import sync_to_async


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
async def addParse(request):
    if request.method == 'POST':
        # Handle file upload
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_obj: TemporaryUploadedFile = request.FILES['file']  # Assuming the file field is named 'file'
            file_content = file_obj.read().decode('utf-8')
        else:
            # return JsonResponse(file_serializer.errors, status=400)
            return JsonResponse(serializer.data, status=201)
        # Handle JSON data
        data = request.data
        data['ticket_number'] = parseInput.objects.count() + 1
        data['client_ip'] = request.META.get('REMOTE_ADDR')
        data['time_created'] = timezone.now()
        data['time_finished'] = timezone.now()
        command = data['parser']
        data['file_content'] = file_content
        print(file_content)
        p_output =  await jc.parse(command, file_content)
        data['p_output'] =  str(p_output)

        serializer = InputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.data, status=201)
        else:
            #return JsonResponse(serializer.errors, status=400)
            return HttpResponse("Hello, async Django!")


async def asynctest():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("http://localhost:8000/api/asynctest/")
        print(r)
@csrf_exempt
async def index(request):
    # print(addParse(request))
    # async with httpx.AsyncClient() as client:
    #     await client.get("http://localhost:8000/api/submit/")
    #     return HttpResponse("Hello, async Django!")
    # loop = asyncio.get_event_loop()
    # async_function = sync_to_async(addParse(request), thread_sensitive=False)
    # await loop.create_task(async_function())
    return HttpResponse("Hello, async Django!")
