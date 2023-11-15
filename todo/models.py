from django.db import models

# Create your models here.
class ToDo(models.Model):
    task = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    status = models.CharField(max_length=200)
    created_at = models.DateField()
