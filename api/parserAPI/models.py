from django.db import models
from datetime import datetime

# Create your models here.

class parseInput(models.Model):
    #title
    p_input = models.CharField(max_length=100)
    time_created = models.DateTimeField(default=datetime.now, blank=True)
    time_finished = models.DateTimeField(null=True, blank=True)
    p_output = models.CharField(max_length=1000)

    def __str__(self):
        #return the task title
        return self.p_input
