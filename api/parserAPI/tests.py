from rest_framework.test import APIClient
from rest_framework import status
from django.test import  TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from parserAPI.models import Ticket
from unittest import mock
from parserAPI.views import parseData

class Test(TestCase):

    def setUp(self):
        # Create an API client object, set up URLs, and creates file data.
        self.client = APIClient()
        self.post_url = reverse("parserAPI:addParse")
        self.parsers_url = reverse("parserAPI:getParsers")
        self.get_url = reverse("parserAPI:instantParse")
        self.file_data = "uid=1000(jjack3032) gid=1000(jjack3032) groups=1000(jjack3032),27(sudo)"

    # Test for a bad parser input.
    def test_bad_parser(self):
        file_obj = SimpleUploadedFile("id_data.txt", self.file_data.encode(), content_type="text/plain")

        data = {
            "parser": "DNE",
            "file": file_obj,
        }
        response = self.client.post(self.post_url, data=data, format="multipart") 

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"error": "Invalid Parser Type"})

    # Test for a bad file input.
    def test_bad_file(self):
        data = {
            "parser": "id",
            "file": "DNE",
        }
        response = self.client.post(self.post_url, data=data, format="multipart") 

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"file": ["The submitted data was not a file. Check the encoding type on the form."]})

    # Test a get request for an invalid ticket number.
    def test_get_nonexistent_ticket(self):
        get_data = {
            "ticket_number": "DNE"
        }

        response = self.client.get(self.get_url, get_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {'error': 'Ticket Not Found'})

    # Test a ticket that would still be in progress.
    @mock.patch('parserAPI.views.threading')
    def test_get_inprogress_ticket(self, mock_threading):
        # Create a mock of a thread.
        mock_thread_instance = mock.Mock()
        mock_threading.Thread.return_value = mock_thread_instance

        # Creates a file and encodes it into a text file.
        file_obj = SimpleUploadedFile("id_data.txt", self.file_data.encode(), content_type="text/plain")

        # Make a post request with a body.
        data = {
            "parser": "id",
            "file": file_obj,
        }
        response = self.client.post(self.post_url, data=data, format="multipart") 

        # Check if post request was successful.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        mock_threading.Thread.assert_called_once()
        mock_thread_instance.start.assert_called_once()
        self.assertIn('ticket_number', response.json())
        self.assertIn('status', response.json())
        self.assertIn('parser', response.json())

        new_ticket = Ticket.objects.get(ticket_number=response.json()['ticket_number'])

        # Manually make the status In Progress.
        new_ticket.update_status("In Progress")

        # Create get request with a body.
        get_data = {
            "ticket_number": response.json()['ticket_number']
        }
        get_response = self.client.get(self.get_url, data=get_data)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertIn('ticket_number', response.json())
        self.assertIn('status', response.json())
        self.assertIn('parser', response.json())

    # Tests a successful post and get request.
    @mock.patch('parserAPI.views.threading')
    def test_successful_post_and_get(self, mock_threading):

        # Create a mock of the thread.
        mock_thread_instance = mock.Mock()
        mock_threading.Thread.return_value = mock_thread_instance

        # Creates a file and encodes it into a text file.
        file_obj = SimpleUploadedFile("id_data.txt", self.file_data.encode(), content_type="text/plain")

        # Make a post request with a body.
        data = {
            "parser": "id",
            "file": file_obj,
        }
        response = self.client.post(self.post_url, data=data, format="multipart") 

        # Check if the post request was saved with the correct fields.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        mock_threading.Thread.assert_called_once()
        mock_thread_instance.start.assert_called_once()
        self.assertIn('ticket_number', response.json())
        self.assertIn('status', response.json())
        self.assertIn('parser', response.json())

        # Get the ticket and add additional fields.
        new_ticket = Ticket.objects.get(ticket_number=response.json()['ticket_number'])
        parseData(self.file_data, new_ticket)

        # Make a get request
        get_data = {
            "ticket_number": response.json()['ticket_number']
        }

    def test_getParsers(self):
        data = b'{"parsers": ["acpi", "airport", "airport_s", "arp", "asciitable", "asciitable_m", "blkid", "bluetoothctl", "cbt", "cef", "certbot", "chage", "cksum", "clf", "crontab", "crontab_u", "csv", "date", "datetime_iso", "df", "dig", "dir", "dmidecode", "dpkg_l", "du", "email_address", "env", "file", "findmnt", "finger", "free", "fstab", "git_log", "git_ls_remote", "gpg", "group", "gshadow", "hash", "hashsum", "hciconfig", "history", "hosts", "id", "ifconfig", "ini", "ini_dup", "iostat", "ip_address", "iptables", "iw_scan", "iwconfig", "jar_manifest", "jobs", "jwt", "kv", "last", "ls", "lsblk", "lsmod", "lsof", "lspci", "lsusb", "m3u", "mdadm", "mount", "mpstat", "netstat", "nmcli", "ntpq", "openvpn", "os_prober", "passwd", "pci_ids", "pgpass", "pidstat", "ping", "pip_list", "pip_show", "plist", "postconf", "proc", "ps", "route", "rpm_qi", "rsync", "semver", "sfdisk", "shadow", "ss", "ssh_conf", "sshd_conf", "stat", "sysctl", "syslog", "syslog_bsd", "systemctl", "systemctl_lj", "systemctl_ls", "systemctl_luf", "systeminfo", "time", "timedatectl", "timestamp", "toml", "top", "tracepath", "traceroute", "udevadm", "ufw", "ufw_appinfo", "uname", "update_alt_gs", "update_alt_q", "upower", "uptime", "url", "ver", "vmstat", "w", "wc", "who", "x509_cert", "xml", "xrandr", "yaml", "zipinfo", "zpool_iostat", "zpool_status"]}'
        response = self.client.get(self.parsers_url)
        self.assertEqual(response.content, data)
        self.assertEqual(response.status_code, 200)