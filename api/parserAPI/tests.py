from django.test import TestCase, RequestFactory, client
from rest_framework.test import APIClient
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
from django.core.files.uploadedfile import SimpleUploadedFile, InMemoryUploadedFile
from django.core.files import File


class Test(TestCase):

    # Tests a successful post request.
    def test_addParse_success(self):
        # Gets the app name and the view function to use.
        url = reverse("parserAPI:addParse")

        # Populate the file with this data.
        file_data = """
                    docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
                            inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
                            ether 02:42:6d:c9:82:46  txqueuelen 0  (Ethernet)
                            RX packets 0  bytes 0 (0.0 B)
                            RX errors 0  dropped 0  overruns 0  frame 0
                            TX packets 0  bytes 0 (0.0 B)
                            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

                    enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
                            inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
                            inet6 fe80::30d4:bdd3:b7d0:3a3e  prefixlen 64  scopeid 0x20<link>
                            ether 08:00:27:c7:e5:37  txqueuelen 1000  (Ethernet)
                            RX packets 21390  bytes 24617735 (24.6 MB)
                            RX errors 0  dropped 0  overruns 0  frame 0
                            TX packets 7691  bytes 1033944 (1.0 MB)
                            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

                    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
                            inet 127.0.0.1  netmask 255.0.0.0
                            inet6 ::1  prefixlen 128  scopeid 0x10<host>
                            loop  txqueuelen 1000  (Local Loopback)
                            RX packets 2565  bytes 1164016 (1.1 MB)
                            RX errors 0  dropped 0  overruns 0  frame 0
                            TX packets 2565  bytes 1164016 (1.1 MB)
                            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
                    """
        
        # Creates a file and encodes it into a text file.
        file_obj = SimpleUploadedFile("ifconfig_data.txt", file_data.encode(), content_type="text/plain")

        # Populate the request body for file uploads.
        data = {
            "parser": "ifconfig",
            "file": file_obj,
        }
        
        # Create an API client object using Django's test.
        client = APIClient()

        # Create a post request that will use the url, data, and the multipart format type for files.
        response = client.post(url, data=data, format="multipart") 

        # Checks if the post request was saved and correct content-type.
        self.assertEqual(response['Content-Type'], "application/json")
        self.assertEqual(response.status_code, 201)