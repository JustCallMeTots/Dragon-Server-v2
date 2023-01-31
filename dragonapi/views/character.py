from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dragonapi.models import character, race, equipment, classes, user, charclass


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
        Equipment = equipment.objects.get(pk=request.data["equipment"])
        
        Character = character.objects.create(
            uid=User,
            name=request.data["name"],
            level=request.data["level"],
            race=Race,
            ability=request.data["ability"],
            description=request.data["description"],
            equipment=Equipment,
            spells=request.data["spells"],
            alive=request.data["alive"]
        )
        for id in request.data["charclasses"]:
            class_id = classes.objects.get(pk=id)
            charclass.objects.create(class_id=class_id, character_id=Character)
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
    
    def destroy(self, request, pk):
        Character = character.objects.get(pk=pk)
        Character.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class CharclassSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = charclass
        depth = 1
        fields = ('class_id', 'character_id')

class CharacterSerializer(serializers.ModelSerializer):
    """JSON serializer for character serializer class determines how the Python data should be serialized to be sent back to the client
    """
    charclasses = CharclassSerializer(many=True)
    class Meta:
        model = character
        fields = ('id', 'uid', 'name', 'level', 'race', 'ability', 'description', 'equipment', 'spells', 'alive', 'charclasses')