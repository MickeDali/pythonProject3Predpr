from .models import Task, User
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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['field_user_subiect', 'field_user_surname', 'field_user_name', 'field_user_name2',
                  'field_user_position', 'field_user_org_name', 'field_user_city', 'field_user_street',
                  'field_user_hauce', 'field_user_phone', 'field_user_email', 'field_user_soglasie']
        widgets = {
            'field_user_subiect': CharField(attrs={
                'class': "form-control",
                'id': "field_user_subiect",
                'aria-describedby': "field_user_subiectHelp",
                'lenght': 50
            }),
            'field_user_surname': CharField(attrs={
                'class': "form-control",
                'id': "field_user_surname",
                'aria-describedby': "field_user_surnameHelp",
                'lenght': 50
            })
            'field_user_name': CharField(attrs={
                'class': "form-control",
                'id': "field_user_name",
                'aria-describedby': "field_user_nameHelp",
                'lenght': 50
            })
            'field_user_name2': CharField(attrs={
                'class': "form-control",
                'id': "field_user_name2",
                'aria-describedby': "field_user_name2Help",
                'lenght': 50
            })
            'field_user_position': CharField(attrs={
                'class': "form-control",
                'id': "field_user_position",
                'aria-describedby': "field_user_positionHelp",
                'lenght': 50
            })
            'field_user_org_name': CharField(attrs={
                'class': "form-control",
                'id': "field_user_org_name",
                'aria-describedby': "field_user_org_nameHelp",
                'lenght': 50
            })
            'field_user_city': CharField(attrs={
                'class': "form-control",
                'id': "field_user_city",
                'aria-describedby': "field_user_cityHelp",
                'lenght': 50
            })
            'field_user_street': CharField(attrs={
                'class': "form-control",
                'id': "field_user_street",
                'aria-describedby': "field_user_streetHelp",
                'lenght': 50
            })
            'field_user_hauce': CharField(attrs={
                'class': "form-control",
                'id': "field_user_hauce",
                'aria-describedby': "field_user_hauceHelp",
                'lenght': 50
            })
            'field_user_phone': CharField(attrs={
                'class': "form-control",
                'id': "field_user_phone",
                'aria-describedby': "field_user_phoneHelp",
                'lenght': 50
            })
            'field_user_email': CharField(attrs={
                'class': "form-control",
                'id': "field_user_email",
                'aria-describedby': "field_user_emailHelp",
                'lenght': 50
            })
            'field_user_soglasie': CharField(attrs={
                'class': "form-control",
                'id': "field_user_soglasie",
                'aria-describedby': "field_user_soglasieHelp",
                'lenght': 50
            })
        }