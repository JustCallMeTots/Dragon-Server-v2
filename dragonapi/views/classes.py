from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dragonapi.models import classes


class ClassesView(ViewSet):
    """Classes view"""

    def retrieve(self, request, pk):
        try:
            Classes = classes.objects.get(pk=pk)
            serializer = ClassesSerializer(Classes)
            return Response(serializer.data)
        except classes.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        Classes = classes.objects.all()
        serializer = ClassesSerializer(Classes, many=True)
        return Response(serializer.data)
      
class ClassesSerializer(serializers.ModelSerializer):
    """JSON serializer for Classes serializer class determines how the Python data should be serialized to be sent back to the client
    """
    class Meta:
        model = classes
        fields = ('hitDie', 'saves', 'class_description', 'classes_name')