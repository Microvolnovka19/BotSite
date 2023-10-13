from django.db import models
import os
import shutil
from django.core.validators import FileExtensionValidator

def get_upload_path(request,filename):
    last = Bots.objects.last()
    try:
        folder = os.scandir("files/{}".format(request.id))
    except:
        folder = None
    if not folder:
        pass
    else:
        shutil.rmtree('files/{}'.format(request.id))
    if (not last):
        os.mkdir("files/{}".format(1))
        new_path = "files/{}/{}".format(1, filename)
    elif last.id == request.id:
        os.mkdir("files/{}".format(last.id))
        new_path = "files/{}/{}".format(last.id, filename)
    else:
        os.mkdir("files/{}".format(last.id+1))
        new_path = "files/{}/{}".format(last.id+1, filename)
    return new_path

def get_id():
    last = Bots.objects.last()
    if (not last):
        new_id = 1
    else:
        new_id = last.id + 1
    return new_id

# Create your models here.
class Bots(models.Model):
    id = models.AutoField(primary_key=True,default=get_id)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=255)
    file = models.FileField(upload_to=get_upload_path,validators=[FileExtensionValidator(allowed_extensions=["csv"])])
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/bots/{}'.format(self.id)
    
    class Meta:
        verbose_name = "Бот"
        verbose_name_plural = 'Боты'

