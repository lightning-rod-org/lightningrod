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
from rest_framework.decorators import api_view


@csrf_exempt
def instantParse(request):
    '''
    List all task snippets
    '''
    if request.method == 'GET':
    #     message = request.GET.get('message', '')

    #     x =  timezone.now()
    #     # Perform the desired operation on p_input
    #     command = "dig " + message + " | jc --dig"
    #     output = subprocess.check_output(command, shell=True, text=True)
    #     numb = parseInput.objects.count() + 1
    #     parse_input = parseInput.objects.create(p_input=message, ticket_number=numb, p_output=output) 
    #    # parse_input.p_input = str(message)
    #     #parse_input['ticket_number'] = parseInput.objects.count() + 1
    #     parse_input.time_created = x
    #     parse_input.time_finished = timezone.now()
        data = JSONParser().parse(request)
        data['ticket_number'] = parseInput.objects.count() + 1
        data['time_created'] = timezone.now()
        data['time_finished'] = None  
        message = data['p_input']
        command = "dig " + message + " | jc --dig"
        data['p_output'] = subprocess.check_output(command, shell=True, text=True)
        serializer = InputSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
         
@csrf_exempt
@api_view(['POST'])

def addParse(request):
    if(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        data['ticket_number'] = parseInput.objects.count() + 1
        data['time_created'] = timezone.now()
        data['time_finished'] = None  
        message = data['p_input']
        command = "dig " + message + " | jc --dig"
        data['p_output'] = subprocess.check_output(command, shell=True, text=True)


        # instanciate with the serializer
        serializer = InputSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)




