from django.db import models

# Create your models here.

class parseInput(models.Model):
    #title
    p_input = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    time_finished = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        #return the task title
        return self.p_input
