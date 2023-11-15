from rest_framework import viewsets
from rest_framework import filters


from .models import *
from .serializers import *


class TodoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["task", "status", "id"]

