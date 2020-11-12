from rest_framework import serializers

from .models import Task
from .models import Tile

class TileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tile
        fields = ('title', 'launch_date', 'status')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'order_field', 'description', 'type', 'tile')