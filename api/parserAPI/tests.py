from django.test import TestCase
from rest_framework.test import APITestCase
import json

# Create your tests here.
class Test(APITestCase):
    def test_does_not_exist(self):
        #response = self.client.post("/test/", {"title": "new idea"}, format="json")
        response = self.client.get("/api/instantParse/test")
        self.assertEqual(response.status_code, 404)

    def test_exists(self):
        response = self.client.get("/api/instantParse/")
        self.assertEqual(response.status_code, 200)

    def test_exist_and_message(self):
        #response = self.client.post("/api/instantParse/", {"title": "new idea"}, format="json")
        response = self.client.get("/api/instantParse/?message='yes'")
        self.assertEqual(response.status_code, 200)

        x = json.loads(response.content)
        
        self.assertEqual(json.loads(response.content))

        #print(json.loads(response.content))

        '''
    def setUp(self):
        self.user = parseInput.objects.create(p_input="1")
        self.user.time_created = 0
        self.user.time_finished = 1
        '''
    '''
    def testcase(self):
        request = self.factory.get("/test/example")

        request.user = self.user

        request.user = AnonymousUser()

        response = instantParse(request)

        self.assertEqual(response.status_code, 200)
    '''

