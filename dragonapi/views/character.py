from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dragonapi.models import character, race, equipment, classes, user


class CharacterView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        try:
            Character = character.objects.get(pk=pk)
            serializer = CharacterSerializer(Character)
            return Response(serializer.data)
        except character.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        Character = character.objects.all()
        serializer = CharacterSerializer(Character, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        creation
        """
        User = user.objects.get(uid=request.data["uid"])
        Race = race.objects.get(pk=request.data["race"])
        Classes = classes.objects.get(pk=request.data["classes_name"])
        Equipment = equipment.objects.get(pk=request.data["equipment"])
        
        Character = character.objects.create(
            uid=User,
            name=request.data["name"],
            level=request.data["level"],
            race=Race,
            classes_name=Classes,
            ability=request.data["ability"],
            description=request.data["description"],
            equipment=Equipment,
            spells=request.data["spells"],
            alive=request.data["alive"]
        )
        serializer = CharacterSerializer(Character)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """_summary_

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """
        
        Character = character.objects.get(pk=pk)
        print(Character)
        User = user.objects.get(uid=request.data["uid"])
        Character.uid = User
        Character.name = request.data["name"]
        Character.level = request.data["level"]
        Race = race.objects.get(pk=request.data["race"])
        Character.race = Race
        Classes = classes.objects.get(pk=request.data["classes_name"])
        Character.classes_name = Classes
        Character.ability = request.data["ability"]
        Character.description = request.data["description"]
        Equipment = equipment.objects.get(pk=request.data["equipment"])
        Character.equipment = Equipment
        Character.spells = request.data["spells"]
        Character.alive = request.data["alive"]
        Character.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class CharacterSerializer(serializers.ModelSerializer):
    """JSON serializer for character serializer class determines how the Python data should be serialized to be sent back to the client
    """
    class Meta:
        model = character
        fields = ('uid', 'name', 'level', 'race', 'classes_name', 'ability', 'description', 'equipment', 'spells', 'alive')