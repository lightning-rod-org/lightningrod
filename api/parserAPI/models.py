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
    ticket_number = models.IntegerField(primary_key=True)
    parser = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='Starting')
    #additional_fields = models.OneToOneField('AdditionalFields', null=True, blank=True, on_delete=models.CASCADE)

    def update_status(self, status):
        self.status = status
        self.save(update_fields=['status'])

class AdditionalFields(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='additional_fields')
    client_ip = models.CharField(max_length=100)
    time_created = models.DateTimeField()
    time_finished = models.DateTimeField()
    p_output = models.JSONField()

class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
