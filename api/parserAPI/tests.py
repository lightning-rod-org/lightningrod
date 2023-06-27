from django.test import TestCase, RequestFactory
from .views import instantParse
from .models import parseInput
from django.urls import reverse
from django.utils import timezone
 

class Test(TestCase):
   def test_does_not_exist(self):
       #response = self.client.post("/test/", {"title": "new idea"}, format="json")
       response = self.client.get("/api/instantParse/test")
       self.assertEqual(response.status_code, 404)

   def test_exists(self):
       factory = RequestFactory()
       data = { 'message' : 'www.dog.com'}
       request= factory.get(reverse(instantParse), data=data)

       response = instantParse(request)
       self.assertEqual(response.status_code, 200)
       obj = parseInput.objects.first()
       self.assertIsNotNone(obj.time_created)

'''
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase
import json

# Create your tests here.
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

