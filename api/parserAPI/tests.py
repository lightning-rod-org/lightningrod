from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class Test(APITestCase):

    def setUp(self):
        # Create an API client object, and gets URL of post view.
        self.client = APIClient()
        self.post_url = reverse("parserAPI:addParse")
    
    # Tests a successful post request.
    def test_addParse_success(self):
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

        # Create a post request that will use the url, data, and the multipart format type for files.
        response = self.client.post(self.post_url, data=data, format="multipart") 

        # Checks if the post request was saved and correct content-type.
        self.assertEqual(response['Content-Type'], "application/json")
        self.assertEqual(response.status_code, 201)

    # Tests to make sure the file serializer works properly.
    def test_addParse_bad_file_format(self):
        file_data = "uid=1000(jjack3032) gid=1000(jjack3032) groups=1000(jjack3032),27(sudo)"
        file_obj = SimpleUploadedFile("id_data.txt", file_data.encode(), content_type="text/plain")

        data = {
            "parser": "id",
            "file": file_obj
        }

        response = self.client.post(self.post_url, data=data, format="json")

        self.assertEqual(response.status_code, 400)
    
    # Tests to make sure a bad parser produces an error.
    def test_addParse_bad_parser(self):
        file_data = "uid=1000(jjack3032) gid=1000(jjack3032) groups=1000(jjack3032),27(sudo)"
        file_obj = SimpleUploadedFile("id_data.txt", file_data.encode(), content_type="text/plain")

        data = {
            "parser": "notValid",
            "file": file_obj
        }

        response = self.client.post(self.post_url, data=data, format="multipart")
        self.assertEqual(response.status_code, 400)