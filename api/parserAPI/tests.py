from django.test import TestCase, RequestFactory, Client
from parserAPI.views import addParse
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

    # Tests a successful post request.
    def test_addParse_success(self):
        # Gets the app name and the view function to use.
        url = reverse('parserAPI:addParse')
        
        # Structure of the data that we want to pass in the response body.
        data = {
            'parser': 'ifconfig',
            'filename': 'ifconfig_data.txt'
        }
        
        # Create a client object using Django's test.
        client = Client()

        # Create a post request that will use the url, data, and the json content type.
        response = client.post(url, data, content_type='application/json')

        # Checks if the post request was saved.
        self.assertEqual(response.status_code, 201)

    def test_addParse_no_content_type(self):
        url = reverse('parserAPI:addParse')

        data = {
            'parser': 'ifconfig',
            'filename': 'ifconfig_data.txt'
        }
        client = Client()

        # No content-type, so this will produce a 400 error, or a bad request error.
        response = client.post(url, data)
        self.assertEqual(response.status_code, 400)
    
    def test_addParse_no_data(self):
        url = reverse('parserAPI:addParse')

        client = Client()

        # No data
        response = client.post(url, data="", content_type="application/json")
        self.assertEqual(response.status_code, 400)

    '''
    def test_addParse_not_valid_parser(self):
        url = reverse('parserAPI:addParse')

        data = {
            'parser': 'helloworld',
            'filename': 'ifconfig_data.txt'
        }
        client = Client()

        # No content-type, so this will produce a 400 error, or a bad request error.
        response = client.post(url, data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        #self.assertEqual(response.content['p_output'], "Parser does not exist")
        print(response.content[])
    
    
    def test_instantParse_success(self):
        url = reverse('parserAPI:addParse')

        data = {
            'parser': 'ifconfig',
            'filename': 'ifconfig_data.txt'
        }
        client = Client()
        response = client.post(url, data, content_type='application/json')
        response = client.get(reverse("parserAPI:instantParse"), data)
        print(response.content)
    '''
