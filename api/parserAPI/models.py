from django.db import models
from datetime import datetime

# Create your models here.

class parseInput(models.Model):
    # title 
    ticket_number = models.IntegerField()
    client_ip = models.CharField(max_length=50)
    time_created = models.DateTimeField(null=True, blank=True)
    time_finished = models.DateTimeField(null=True, blank=True)
    p_output = models.CharField(max_length=1000000)
    parser = models.CharField(max_length=50)

    def __str__(self):
        return self.parser
    file_content = models.CharField(max_length=1000000)


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name
