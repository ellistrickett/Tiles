from rest_framework import serializers

from .models import Task
from .models import Tile

class TileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tile
        fields = ('id', 'title', 'launch_date', 'status')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'order_field', 'description', 'type', 'tile')