from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Customer, Implementer, ServiceObject, Order
from .forms import TaskForm, UserForm, CustomerForm, ImplementerForm, ServiceObjectForm, OrderForm

#from django.urls import re_path as url
#from rest_framework_swagger.views import get_swagger_view

#schema_view = get_swagger_view(title='Pastebin API')

#urlpatterns = [
#    url(r'^$', schema_view)
#]
##### REST from rest_framework import viewsets
##### REST from .serializers import TaskSerializer
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    #users = User.objects.all()
    return render(request, 'organizer/index.html', {
        "title": "Органайзер",
        "header": "Список дел",
        "tasks": tasks
    })
    #return HttpResponse(html_template)



def contacts(request):
    return render(request, 'organizer/contacts.html')

def task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'organizer/task.html', context)

def regist(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'organizer/regist.html', context)

def customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    form = CustomerForm()
    context = {
        'form': form
    }
    return render(request, 'organizer/customer.html', context)

def implementer(request):
    if request.method == "POST":
        form = ImplementerForm(request.POST)
        if form.is_valid():
            form.save()
    form = ImplementerForm()
    context = {
        'form': form
    }
    return render(request, 'organizer/implementer.html', context)

def service_object(request):
    if request.method == "POST":
        form = ServiceObjectForm(request.POST)
        if form.is_valid():
            form.save()
    form = ServiceObjectForm()
    context = {
        'form': form
    }
    return render(request, 'organizer/service_object.html', context)

def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'organizer/order.html', context)

##### REST class TaskViewSet(viewsets.ModelViewSet):
##### REST     queryset = Task.objects.all().order_by('id')
##### REST     serializer_class = TaskSerializer