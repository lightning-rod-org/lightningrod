from rest_framework import routers,serializers,viewsets
from .models import parseInput
class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parseInput
        fields = ['ticket_number', 'p_input', 'time_created', 'time_finished', 'p_output']
