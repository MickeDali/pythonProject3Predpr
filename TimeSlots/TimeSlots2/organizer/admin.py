from django.contrib import admin

from .models import Task, Customer, Implementer, ServiceObject, Order
# Register your models here.

admin.site.register(Task)
admin.site.register(Customer)
admin.site.register(Implementer)
admin.site.register(ServiceObject)
admin.site.register(Order)

