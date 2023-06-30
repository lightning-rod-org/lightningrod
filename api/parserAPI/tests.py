from django.test import TestCase, RequestFactory
from .views import instantParse
from .models import parseInput
from django.urls import reverse
from django.utils import timezone

class Test(TestCase):
    def test_does_not_exist(self):
       #response = self.client.post("/test/", {"title": "new idea"}, format="json")
       factory = RequestFactory()

       req = factory.get("/api/instantParse/test")
       #print("THIS IS REQ:" + str(req))
       response = instantParse(req)
       self.assertEqual(response.status_code, 404)

    def test_exists(self):
       factory = RequestFactory()
       data = { 'message' : 'www.dog.com'}
       request= factory.get(reverse(instantParse), data=data)

       response = instantParse(request)
       self.assertEqual(response.status_code, 200)
       obj = parseInput.objects.first()
       self.assertIsNotNone(obj.time_created)


    #TODO 

#    def test_add_parse(self):
#         # Create a POST request
#         data = {
#             'p_input': 'example input',
#         }
#         request = self.factory.post(reverse(addParse), data=data)
        
#         # Mock the subprocess check_output result
#         subprocess_result = "example output"
#         subprocess_mock = subprocess.Mock(return_value=subprocess_result)
#         with subprocess.patch('subprocess.check_output', subprocess_mock):
#             # Make the request to the view
#             response = addParse(request)
        
#         # Assert the response status code
#         self.assertEqual(response.status_code, 201)
        
#         # Assert that the object was saved to the database
#         self.assertEqual(parseInput.objects.count(), 1)
        
#         # Assert the object's attributes
#         obj = parseInput.objects.first()
#         self.assertEqual(obj.p_input, 'example input')
#         self.assertIsNotNone(obj.time_created)
#         #this is gonna need to be changed later once the time_finished gets 
#         #properly added
#         self.assertIsNone(obj.time_finished)
#         self.assertEqual(obj.p_output, subprocess_result)


'''
from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework.parsers import JSONParser
import subprocess
from .views import addParse
from .models import parseInput
import subprocess

class AddParseTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_add_parse(self):
        # Create a POST request
        data = {
            'p_input': 'example input',
        }
        request = self.factory.post(reverse(addParse), data=data)
        
        # Mock the subprocess check_output result
        subprocess_result = "example output"
        subprocess_mock = subprocess.Mock(return_value=subprocess_result)
        with subprocess.patch('subprocess.check_output', subprocess_mock):
            # Make the request to the view
            response = addParse(request)
        
        # Assert the response status code
        self.assertEqual(response.status_code, 201)

from rest_framework import status
from rest_framework.test import APITestCase
import json
        
        # Assert that the object was saved to the database
        self.assertEqual(parseInput.objects.count(), 1)
        
        # Assert the object's attributes
        obj = parseInput.objects.first()
        self.assertEqual(obj.p_input, 'example input')
        self.assertIsNotNone(obj.time_created)
        #this is gonna need to be changed later once the time_finished gets 
        #properly added
        self.assertIsNone(obj.time_finished)
        self.assertEqual(obj.p_output, subprocess_result)
class Test(APITestCase):
    def test_does_not_exist(self):
        #response = self.client.post("/test/", {"title": "new idea"}, format="json")
        response = self.client.get("/api/instantParse/test")
        self.assertEqual(response.status_code, 404)

    def test_exists(self):
        message = {"message": "www.dog.com"}
        response = self.client.get("/api/instantParse/", message)
        self.assertEqual(response.status_code, 200)

    
    def test_post_success(self):
        data = {'title': 'hello'}
        response = self.client.post("/api/instantParse/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_post_error(self):
        response = self.client.post("/api/instantParse/test", {"title": "hi"}, format="json")
        self.assertEqual(response.status_code, 404)

    def test_exist_and_message(self):
        #response = self.client.post("/api/instantParse/", {"title": "new idea"}, format="json")
        response = self.client.get("/api/instantParse/?message='yes'")
        self.assertEqual(response.status_code, 200)

        x = json.loads(response.content)
        
        self.assertEqual(json.loads(response.content))

        #print(json.loads(response.content))
    '''

