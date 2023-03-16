from django.urls import path, include
from . import views
##### REST from rest_framowork import routers


##### REST router = routers.DefaultRouter()
##### REST router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', views.index),
    path('contacts', views.contacts, name='contacts'),
    path('task', views.task, name='task'),
    path('index', views.index, name='index'),
    path('regist', views.index, name='regist'),
    ##### REST patch('api/', include(router.urls))
    ##### REST     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]