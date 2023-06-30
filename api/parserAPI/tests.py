from django.test import TestCase, RequestFactory
from .views import instantParse
from .models import parseInput
from django.urls import reverse
from django.utils import timezone
from parserAPI import views
import subprocess
from django.http import HttpRequest

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
    
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_add_parse_fields(self):
        data = {
            'p_input': 'example_input',
            # Add any other necessary fields
        }

        request = self.factory.get("/api/instantParse/", data=data)
        request.p_input = "www.dog.com"
        response = views.instantParse(request)
        
        self.assertEquals(response.status_code, 200)

