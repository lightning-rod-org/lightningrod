from rest_framework import routers, serializers, viewsets
from .models import parseInput, File


class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parseInput
        fields = ['ticket_number', 'client_ip', 'parser', 'time_created', 'p_output', 'time_finished', 'file_content']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
