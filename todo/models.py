from django.db import models
from datetime import datetime

def upload_middleware(instance,filename):
    filebase,fileExtention = filename.split(".")
    return "images/%s_%s.%s" % (str(instance.id),str(datetime.now()),fileExtention)

# Create your models here.
class ToDo(models.Model):
    task = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    status = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=upload_middleware,null=True, blank=True, default="")
    created_at = models.DateField()
