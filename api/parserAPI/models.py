from django.db import models


# Create your models here.
class Ticket(models.Model):
    ticket_number = models.CharField(max_length=36, primary_key=True)
    parser = models.CharField(max_length=100, default='unknown')
    status = models.CharField(max_length=100, default='Starting')

    def update_status(self, status):
        self.status = status
        self.save(update_fields=['status'])


class FinalTicket(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='final_tick')
    client_ip = models.CharField(max_length=100)
    time_created = models.DateTimeField()
    time_finished = models.DateTimeField()
    p_output = models.JSONField()
    parser = models.CharField(max_length=100, default='unknown')


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name

# class FinalTicket(models.Model):
#     first_ticket = models.OneToOneField(Ticket,default=None, on_delete=models.CASCADE, related_name='FinalTicket')
#     client_ip = models.CharField(max_length=100)
#     time_created = models.DateTimeField()
#     time_finished = models.DateTimeField()
#     p_output = models.JSONField()