# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from .serializers import InputSerializer
# Task model
from .models import parseInput
import os
import subprocess
from datetime import datetime
from django.utils import timezone


@csrf_exempt
def instantParse(request):
    '''
    List all task snippets
    '''
    if request.method == 'GET':
        message = request.GET.get('message', '')
        x =  timezone.now()
        # Perform the desired operation on p_input
        command = "dig " + message + " | jc --dig"
        output = subprocess.check_output(command, shell=True, text=True)

        parse_input = parseInput.objects.create(p_input=output)
        parse_input.time_created = x
        parse_input.time_finished = timezone.now()

        serializer = InputSerializer(parse_input)
        return JsonResponse(serializer.data)

    # elif(request.method == 'POST'):
    #     # parse the incoming information
    #     data = JSONParser().parse(request)
    #     # instanciate with the serializer
    #     serializer = InputSerializer(data=data)
    #     # check if the sent information is okay
    #     if(serializer.is_valid()):
    #         # if okay, save it on the database
    #         serializer.save()
    #         # provide a Json Response with the data that was saved
    #         return JsonResponse(serializer.data, status=201)
    #         # provide a Json Response with the necessary error information
    #     return JsonResponse(serializer.errors, status=400)

'''
def findParse(request):
    
    List all task snippets
    
    if request.method == 'GET':
        message = request.GET.get('message', '')
        x =  timezone.now()
        # Perform the desired operation on p_input
        command = "find " + message + " | jc --find"
        output = subprocess.check_output(command, shell=True, text=True)

        parse_input = parseInput.objects.create(p_input=output)
        parse_input.time_created = x
        parse_input.time_finished = timezone.now()

        serializer = InputSerializer(parse_input)
        return JsonResponse(serializer.data)
'''
@csrf_exempt
def addParse(request):
    '''
    List all task snippets
    '''
    # if(request.method == 'GET'):
    #     # get all the tasks
    #     x =  timezone.now()
    #     tasks = parseInput.objects.all()
    #     # serialize the task data
    #     command = "dig " + message + " | jc --dig"
    #     output = subprocess.check_output(command, shell=True, text=True)
    #     parse_input = parseInput.objects.create(p_input=output)

    #     serializer = InputSerializer(tasks, many=True)
    #     # return a Json response
    #     return JsonResponse(serializer.data,safe=False)
    if request.method == 'GET':
        message = request.GET.get('message', '')
        command = "dig " + message + " | jc --dig"
        output = subprocess.check_output(command, shell=True, text=True)

        parse_input = parseInput.objects.create(p_input=output, time_created=timezone.now(), time_finished=timezone.now())
        parse_input.save()

        serializer = InputSerializer(parse_input)
        return JsonResponse(serializer.data, status=201)
    
    # Handle other HTTP methods if needed

    # Return a default response if none of the conditions above are met
    return JsonResponse({'message': 'Invalid request'}, status=400)

