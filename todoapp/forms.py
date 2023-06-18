from django.forms import models
from .models import Task
from django import forms

class TaskForm(models.ModelForm):
    text = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

    class Meta:
        model = Task
        fields = ["text", "complete"]
        