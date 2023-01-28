from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dragonapi.models import equipment


class EquipmentView(ViewSet):
    """equipment view"""

    def retrieve(self, request, pk):
        try:
            Equipment = equipment.objects.get(pk=pk)
            serializer = EquipmentSerializer(Equipment)
            return Response(serializer.data)
        except equipment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        Equipment = equipment.objects.all()
        serializer = EquipmentSerializer(Equipment, many=True)
        return Response(serializer.data)
      
class EquipmentSerializer(serializers.ModelSerializer):
    """JSON serializer for equipment serializer class determines how the Python data should be serialized to be sent back to the client
    """
    class Meta:
        model = equipment
        fields = ('weapon_name', 'weapon_type', 'weapon_description')