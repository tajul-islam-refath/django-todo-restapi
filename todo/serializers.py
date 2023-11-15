from rest_framework import serializers
from .models import *

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
    
    def create(self,data):
        todo = ToDo(
            task = data['task'],
            description = data['description'],
            status = data['status'],
            created_at = data['created_at']
        )
        todo.save()
        return todo