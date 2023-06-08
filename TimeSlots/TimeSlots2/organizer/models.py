from django.db import models
import time

sec = time.time()

# Create your models here.
class Task(models.Model):
    title = models.CharField('Title', max_length=180)
    description = models.TextField('Description', max_length=256)
    time_creat = time.localtime()
    time_start = time.localtime()
    time_stop = time.localtime()

    def str(self):
        return self.title

class User(models.Model):
    __last_id = 0
    __list = dict()
    #User.__last_id += 1
    #self.id = User.__last_id

    #field_user_subject = models.CharField('user_subject', max_length=20, help_text="Выбирите тип регистрации")
    field_user_surname = models.CharField('user_surname', max_length=20, help_text="Введите фамилию")
    field_user_name = models.CharField('user_name', max_length=20, help_text="Введите имя")
    field_user_name2 = models.CharField('user_name2', max_length=20, help_text="Введите отчество")
    field_user_position = models.CharField('user_position', max_length=20, help_text="Введите должность")
    field_user_org_name = models.CharField('user_org_name', max_length=20, help_text="Введите название организации")
    field_user_city = models.CharField('user_city', max_length=20, help_text="Введите город")
    field_user_street = models.CharField('user_street', max_length=20, help_text="Введите название улицы")
    field_user_hauce = models.CharField('user_hauce', max_length=20, help_text="Введите номер дома, корпус и т.д.")
    field_user_phone = models.CharField('user_phone', max_length=20, help_text="Введите номер телефона")
    field_user_email = models.CharField('user_email', max_length=20, help_text="Введите электронную почту")
    #field_user_soglasie = models.CharField('user_soglasie', max_length=20, help_text="Установите флажок, если согласны")

    field_user_created = time.time()
    field_user_last_vizit = field_user_created
    field_user_updated = None


