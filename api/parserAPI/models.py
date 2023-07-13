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

class Ticket(models.Model):
    ticket_number = models.IntegerField()
    parser = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default="Starting")

    def is_completed(self):
        return self.status == "Completed"
    
    def all_data(self):
        if self.is_completed():
            print("hi")
        return {}
    
class AdditionalFields(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    client_ip = models.CharField(max_length=50)
    time_created = models.DateTimeField(null=True, blank=True)
    time_finished = models.DateTimeField(null=True, blank=True)
    parser = models.CharField(max_length=50)
    p_output = models.JSONField()

class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
