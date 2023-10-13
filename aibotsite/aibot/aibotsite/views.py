from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import BotsForm  
from django import forms
from .models import Bots
from django.http import FileResponse, HttpResponse
import os
import shutil
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

# Create your views here.
def index(request):
    return render(request, 'main.html')

def bots(request):
    bots = Bots.objects.all()
    new_button = [{"additional_url":"upload", "additional_name":"Добавить бота"},]
    context = {
        "bots":bots,
        "additional":new_button,
    }
    check_paths()
    return render(request, 'bots.html',context)

def bot_upload(request):
    error = None
    if request.method == 'POST':
        form = BotsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            bot = Bots.objects.last()
            return redirect('bots')
        else:
            error = "Неподдерживаемый формат файла. Допустимый: .csv"
            #print("4to-to poshlo ne tak v processe 3agruzki")
    else:
        form = BotsForm()
    return render(request, 'upload.html', {
        'form': form, 'error': error
    })

class BotsDetailView(DetailView):
    model = Bots
    template_name = "bot_read.html"
    context_object_name = "bot"

class BotsDeleteView(DeleteView):
    model = Bots
    template_name = "delete.html"
    success_url = "../../"

class BotsUpdateView(UpdateView):
    model = Bots
    template_name = "upload.html"
    form_class = BotsForm

def download(request, pk):
    obj = Bots.objects.get(id=pk)
    filename = str(obj.file)
    response = FileResponse(open(filename, 'rb'))
    return response

def check_paths():
    bots = Bots.objects.all()
    folds = os.scandir("files/")
    existing_ids = list()
    for i in bots:
        existing_ids.append(i.id)

    for i in folds:
        if int(i.name) not in existing_ids:
            shutil.rmtree('files/{}'.format(i.name))


### API 

@api_view(['GET'])
def get_file(request, pk):
    if request.method == "GET":
        obj = Bots.objects.get(id=pk)
        filename = str(obj.file)
        return FileResponse(open(filename, 'rb'))
    
    
class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bots
        fields = ['id', 'name','author','short_desc']
    
class BotSerializerFile(serializers.ModelSerializer):
    class Meta:
        model = Bots
        fields = ['id', 'name','author','short_desc','file']
        
class SerializerFile(serializers.ModelSerializer):
    class Meta:
        model = Bots
        fields = ['file']

class BotList(generics.ListAPIView):
    queryset = Bots.objects.all()
    serializer_class = BotSerializer
    renderer_classes = [JSONRenderer]

class BotDetail(generics.RetrieveAPIView):
    queryset = Bots.objects.all()
    serializer_class = BotSerializerFile
    renderer_classes = [JSONRenderer]

class BotDestroy(generics.DestroyAPIView):
    queryset = Bots.objects.all()
    serializer_class = BotSerializer
    renderer_classes = [JSONRenderer]

    def delete(self, request, pk):
        instance = self.get_object()
        self.perform_destroy(instance)
        return(HttpResponse("Deleted :)"))
    

class BotCreateView(generics.CreateAPIView):
    queryset = Bots.objects.all()
    serializer_class = BotSerializer
    renderer_classes = [JSONRenderer]

class BotUploadFileView(generics.UpdateAPIView):
    queryset = Bots.objects.all()
    serializer_class = SerializerFile
    renderer_classes = [JSONRenderer]

class BotEditView(generics.UpdateAPIView):
    queryset = Bots.objects.all()
    serializer_class = BotSerializer
    renderer_classes = [JSONRenderer]
