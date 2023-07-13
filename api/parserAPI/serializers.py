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

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["ticket_number", "parser", "status"]

class AdditionalFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalFields
        fields = ["ticket", "client_ip", "time_created", "time_finished", "parser", "p_output"]