from django.urls import path, include
from . import views
##### REST from rest_framowork import routers
from django.urls import re_path as url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
##### REST router = routers.DefaultRouter()
##### REST router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', views.index),
    path('contacts', views.contacts, name='contacts'),
    path('task', views.task, name='task'),
    path('index', views.index, name='index'),
    path('regist', views.regist, name='regist'),
    path('view', schema_view),
    ##### REST patch('api/', include(router.urls))
    ##### REST     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]