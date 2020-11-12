from rest_framework import viewsets

from .serializers import TileSerializer
from .models import Tile

from .serializers import TaskSerializer
from .models import Task

class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all().order_by('title')
    serializer_class = TileSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('title')
    serializer_class = TaskSerializer