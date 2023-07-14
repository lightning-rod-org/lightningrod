from rest_framework import routers, serializers, viewsets
from .models import parseInput, File, Ticket, AdditionalFields


class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parseInput
        fields = ["ticket_number", "client_ip", "parser", "time_created", "p_output", "time_finished"]


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class AdditionalFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalFields
        fields = ['client_ip', 'time_created', 'time_finished', 'p_output']

class TicketSerializer(serializers.ModelSerializer):

    #additional_fields = AdditionalFieldsSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ['ticket_number', 'parser', 'status']