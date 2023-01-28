from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dragonapi.models import race


class RaceView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        try:
            Race = race.objects.get(pk=pk)
            serializer = RaceSerializer(Race)
            return Response(serializer.data)
        except race.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        Race = race.objects.all()
        serializer = RaceSerializer(Race, many=True)
        return Response(serializer.data)
      
class RaceSerializer(serializers.ModelSerializer):
    """JSON serializer for race serializer class determines how the Python data should be serialized to be sent back to the client
    """
    class Meta:
        model = race
        fields = ('race_name', 'race_description', 'ability_increase')