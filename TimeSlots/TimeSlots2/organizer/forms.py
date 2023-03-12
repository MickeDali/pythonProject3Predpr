from .models import Task
from django.forms import ModelForm,TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'id': "title",
                'aria-describedby': "titleHelp",
                'lenght': 50
            }),
            'description': TextInput(attrs={
                'class': "form-control",
                'id': "description",
                'aria-describedby': "descriptionHelp",
                'lenght': 50
            })
        }