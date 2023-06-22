from .models import Task, User, ServiceObject
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


class OrderForm(ModelForm):
    class Meta:
        model = ServiceObject
        fields = ['name', 'title', 'service_type', 'status', 'implementers_list', 'client']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'id': "name",
                'aria-describedby': "nameHelp",
                'lenght': 50
            }),
            'title': TextInput(attrs={
                'class': "form-control",
                'id': "title",
                'aria-describedby': "titleHelp",
                'lenght': 50
            }),
            'service_type': TextInput(attrs={
                'class': "form-control",
                'id': "service_type",
                'aria-describedby': "service_typeHelp",
                'lenght': 50
            }),
            'status': TextInput(attrs={
                'class': "form-control",
                'id': "status",
                'aria-describedby': "statusHelp",
                'lenght': 50
            }),
            'implementers_list': TextInput(attrs={
                'class': "form-control",
                'id': "implementers_list",
                'aria-describedby': "implementers_listHelp",
                'lenght': 50
            }),
            'client': TextInput(attrs={
                'class': "form-control",
                'id': "client",
                'aria-describedby': "clientHelp",
                'lenght': 50
            })
        }

