from django.db import models
from datetime import datetime


# Create your models here.

class parseInput(models.Model):
    # title 
    ticket_number = models.IntegerField()
    client_ip = models.CharField(max_length=50)
    time_created = models.DateTimeField(null=True, blank=True)
    time_finished = models.DateTimeField(null=True, blank=True)
    parser = models.CharField(max_length=50)
    p_output = models.JSONField()

    def __str__(self):
        return self.parser

    file_content = models.CharField(max_length=1500)


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
