from .models import Task, User, ServiceObject, Customer, Implementer, Order
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


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'surname', 'phone', 'service_type', 'service_objects_list']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'id': "name",
                'aria-describedby': "nameHelp",
                'lenght': 50
            }),
            'surname': TextInput(attrs={
                'class': "form-control",
                'id': "surname",
                'aria-describedby': "surnameHelp",
                'lenght': 50
            }),
            'phone': TextInput(attrs={
                'class': "form-control",
                'id': "phone",
                'aria-describedby': "phoneHelp",
                'lenght': 50
            }),
            'service_type': TextInput(attrs={
                'class': "form-control",
                'id': "service_type",
                'aria-describedby': "service_typeHelp",
                'lenght': 50
            }),
            'service_objects_list': TextInput(attrs={
                'class': "form-control",
                'id': "service_objects_list",
                'aria-describedby': "service_objects_listHelp",
                'lenght': 50
            })
        }


class ImplementerForm(ModelForm):
    class Meta:
        model = Implementer
        fields = ['name', 'surname', 'phone', 'service_type', 'service_objects_list', 'rating', 'title', 'description', 'mobile', 'type_of_work', 'type_of_system', 'qualification']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'id': "name",
                'aria-describedby': "nameHelp",
                'lenght': 50
            }),
            'surname': TextInput(attrs={
                'class': "form-control",
                'id': "surname",
                'aria-describedby': "surnameHelp",
                'lenght': 50
            }),
            'phone': TextInput(attrs={
                'class': "form-control",
                'id': "phone",
                'aria-describedby': "phoneHelp",
                'lenght': 50
            }),
            'service_type': TextInput(attrs={
                'class': "form-control",
                'id': "service_type",
                'aria-describedby': "service_typeHelp",
                'lenght': 50
            }),
            'service_objects_list': TextInput(attrs={
                'class': "form-control",
                'id': "service_objects_list",
                'aria-describedby': "service_objects_listHelp",
                'lenght': 50
            }),
            'rating': TextInput(attrs={
                'class': "form-control",
                'id': "rating",
                'aria-describedby': "ratingHelp",
                'lenght': 50
            }),
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
            }),
            'mobile': TextInput(attrs={
                'class': "form-control",
                'id': "mobile",
                'aria-describedby': "mobileHelp",
                'lenght': 50
            }),
            'type_of_work': TextInput(attrs={
                'class': "form-control",
                'id': "type_of_work",
                'aria-describedby': "type_of_workHelp",
                'lenght': 50
            }),
            'type_of_system': TextInput(attrs={
                'class': "form-control",
                'id': "type_of_system",
                'aria-describedby': "type_of_systemHelp",
                'lenght': 50
            }),
            'qualification': TextInput(attrs={
                'class': "form-control",
                'id': "qualification",
                'aria-describedby': "qualificationHelp",
                'lenght': 50
            })
        }

class ServiceObjectForm(ModelForm):
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

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['desired_implementer', 'implementer', 'service_object', 'service_type', 'status', 'description', 'desired_execution_time']
        widgets = {
            'desired_implementer': TextInput(attrs={
                'class': "form-control",
                'id': "desired_implementer",
                'aria-describedby': "desired_implementerHelp",
                'lenght': 50
            }),
            'implementer': TextInput(attrs={
                'class': "form-control",
                'id': "implementer",
                'aria-describedby': "implementerHelp",
                'lenght': 50
            }),
            'service_object': TextInput(attrs={
                'class': "form-control",
                'id': "service_object",
                'aria-describedby': "service_objectHelp",
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
            'desired_execution_time': TextInput(attrs={
                'class': "form-control",
                'id': "desired_execution_time",
                'aria-describedby': "desired_execution_timeHelp",
                'lenght': 50
            })
        }
