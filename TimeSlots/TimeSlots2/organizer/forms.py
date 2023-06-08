from .models import Task, User
from django.forms import ModelForm,TextInput, CharField

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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['field_user_surname', 'field_user_name', 'field_user_name2',
                  'field_user_position', 'field_user_org_name', 'field_user_city', 'field_user_street',
                  'field_user_hauce', 'field_user_phone', 'field_user_email']
