from rest_framework import serializers
from .models import File, Ticket, AdditionalFields

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class AdditionalFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalFields
        fields = ['client_ip', 'time_created', 'time_finished', 'p_output']

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['ticket_number', 'parser', 'status']