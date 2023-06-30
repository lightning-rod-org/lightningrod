from django.test import TestCase, RequestFactory
from .views import instantParse
from .models import parseInput
from django.urls import reverse
from django.utils import timezone
<<<<<<< Updated upstream
=======
from django.views import addParse
import subprocess
from django.http import HttpRequest
from parserAPI.views import addParse
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream

=======
        
   def test_add_parse_fields(self):
        # Create a dummy HTTP POST request
        request = HttpRequest()
        request.method = 'POST'
        request.META['REMOTE_ADDR'] = '127.0.0.1'
        # Add any other necessary request parameters
>>>>>>> Stashed changes

        # Perform the view function call
        response = addParse(request)

        # Assert that the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Assert that the parsed input fields have the expected values
        data = response.json()
        self.assertEqual(data['ticket_number'], parseInput.objects.count() + 1)
        self.assertEqual(data['client_ip'], '127.0.0.1')
        # Add assertions for other fields as needed


