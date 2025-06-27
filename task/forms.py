from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user']
        widgets = {
            'due_date': forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
            'due_time': forms.TimeInput(attrs={'class' : 'form-control', 'type' : 'time'}),
        }