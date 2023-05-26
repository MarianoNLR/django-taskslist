from django.forms import ModelForm
from django import forms
from .models import Task, Project
class CreateTaskForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Titulo"}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={"placeholder": "Ingrese la descripcion", "rows": "5"}))
    class Meta:
        model = Task
        fields = ['title', 'description']
        
class CreateProjectForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Titulo"}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={"placeholder": "Ingrese la descripcion", "rows": "5"}))
    class Meta:
        model = Project
        fields = ['title', 'description']
