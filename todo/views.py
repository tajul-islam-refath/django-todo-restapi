from rest_framework import viewsets
from rest_framework import filters


from .models import *
from .serializers import *


class TodoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    print(queryset)
    serializer_class = ToDoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["task", "status", "id"]

class AddTodoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def post(self,request):
        print(f"request {request}")
        serializer = ToDoSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'result':serializer})
        return Response({'result':"fail"})






