from .models import Task, User
from django.forms import ModelForm,TextInput, CharField

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']#, 'time_create', 'time_start', 'time_stop']
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
            })#,
            # 'time_create': TextInput(attrs={
            #     'class': "form-control",
            #     'id': "time_create",
            #     'aria-describedby': "timecreateHelp",
            #     'lenght': 50
            # }),
            # 'time_start': TextInput(attrs={
            #     'class': "form-control",
            #     'id': "time_start",
            #     'aria-describedby': "timestartHelp",
            #     'lenght': 50
            # }),
            # 'time_stop': TextInput(attrs={
            #     'class': "form-control",
            #     'id': "time_stop",
            #     'aria-describedby': "timestopHelp",
            #     'lenght': 50
            # })
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['field_user_surname', 'field_user_name', 'field_user_name2',
                  'field_user_position', 'field_user_org_name', 'field_user_city', 'field_user_street',
                  'field_user_hauce', 'field_user_phone', 'field_user_email']
