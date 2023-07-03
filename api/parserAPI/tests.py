from django.test import TestCase, RequestFactory
from .views import instantParse
from .models import parseInput
from django.urls import reverse
import os
import json
from django.utils import timezone
from parserAPI import views
import subprocess
from django.http import HttpRequest
from .models import parseInput
import unittest

class Test(TestCase):
    # def test_does_not_exist(self):
    #    #response = self.client.post("/test/", {"title": "new idea"}, format="json")
    #    factory = RequestFactory()

    #    req = factory.get("/api/instantParse/test")
    #    #print("THIS IS REQ:" + str(req))
    #    response = instantParse(req)
    #    self.assertEqual(response.status_code, 404)

    # def test_exists(self):
    #    factory = RequestFactory()
    #    data = { 'message' : 'www.dog.com'}
    #    request= factory.get(reverse(instantParse), data=data)

    #    response = instantParse(request)
    #    self.assertEqual(response.status_code, 200)
    #    obj = parseInput.objects.first()
    #    self.assertIsNotNone(obj.time_created)
    
    # def setUp(self):
    #     # Every test needs access to the request factory.
    #     self.factory = RequestFactory()

    def empty_field_test(self):
        # # Create a dummy GET request with data as query parameters
        # factory = RequestFactory()
        # request = factory.get('/api/instantParse/')
        # request.data = {"p_input "}
        data = {"p_input": ""}
        # Perform the view function call
        current_directory = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(current_directory, 'addparse.json')
        with open(json_file_path) as file:
            json_data = json.load(file)
        test = json_data["p_input"]
        command = "dig " + test + " | jc --dig"

        empty_input = parseInput.objects.create(ticket_number = 1, client_ip= "127.0.01.", time_created=  "2023-06-30T14:25:26.191774Z", time_finished = "2023-06-30T14:25:26.191778Z", p_input = "", p_output= command)

        self.assertTrue(2==3)

