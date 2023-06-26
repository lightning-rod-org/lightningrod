from rest_framework import routers,serializers,viewsets
from .models import parseInput
class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parseInput
        fields = ['p_input', 'time_created', 'time_finished']
