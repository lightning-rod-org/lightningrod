from rest_framework import serializers
from .models import File, Ticket, FinalTicket

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class FinalTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalTicket
        fields = ['ticket', 'client_ip', 'time_created', 'time_finished', 'p_output', 'parser']

class TicketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ticket
        fields = ['ticket_number', 'parser', 'status']

# class FinalTicketSerializer(serializers.ModelSerializer):
#     model = FinalTicket
#     fields = ['first_ticket', 'client_ip', 'time_created', 'time_finished', 'p_output']
