from django import forms
from .models import Bots
from django.forms import ModelForm, TextInput, FileInput
class BotsForm(forms.ModelForm):
    class Meta:
        model = Bots
        fields = ('name', 'author', "short_desc", "file")

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Имя бота',
            }),
            'short_desc': TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Короткое описание(не длиннее 255)'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Автор'
            }),
            'file': FileInput(attrs={
                'class': 'form-control',
                'placeholder':'Файл для загрузки'
            })}