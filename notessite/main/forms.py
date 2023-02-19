from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model =  Task
        fields = ('title', 'task')
        widgets = {'title': TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'введите название'}),
                   'task': TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'введите описание'})}










