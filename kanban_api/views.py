from rest_framework import viewsets
from .models import Kanban
from .serializers import KanbanSerializer

class KanbanViewSet(viewsets.ModelViewSet):
    queryset = Kanban.objects.all()
    serializer_class = KanbanSerializer