from django.db import models
import time

sec = time.time()

# Create your models here.
class Task(models.Model):
    title = models.CharField('Title', max_length=180)
    description = models.TextField('Description', max_length=256)

    def str(self):
        return self.title

class User(models.Model):
    __last_id = 0
    __list = dict()
    #User.__last_id += 1
    #self.id = User.__last_id

    subiect = models.CharField(max_length=20, help_text="Выбирите тип регистрации")
    surname = models.CharField(max_length=20, help_text="Введите фамилию")
    name = models.CharField(max_length=20, help_text="Введите имя")
    field_user_name2 = models.CharField(max_length=20, help_text="Введите отчество")
    field_user_position = models.CharField(max_length=20, help_text="Введите должность")
    field_user_org_name = models.CharField(max_length=20, help_text="Введите название организации")
    field_user_city = models.CharField(max_length=20, help_text="Введите город")
    field_user_street = models.CharField(max_length=20, help_text="Введите название улицы")
    field_user_hauce = models.CharField(max_length=20, help_text="Введите номер дома, корпус и т.д.")
    field_user_phone = models.CharField(max_length=20, help_text="Введите номер телефона")
    field_user_email = models.CharField(max_length=20, help_text="Введите электронную почту")
    field_user_soglasie = models.CharField(max_length=20, help_text="Установите флажок, если согласны")
    field_user_regist = models.CharField(max_length=20, help_text="Зарегистрироваться")

    field_user_created = time.time()
    field_user_last_vizit = field_user_created
    field_user_updated = None

    @property
    def phone(self):
        return self.__phone
    @staticmethod
    def get_user_by_id(id):
        for user in User.__list():
            if user.id == id:
                return user
        raise ValueError("Пользователь не найден")

    @staticmethod
    def get_user_by_phone(phone):
        for user in User.__list():
            if user.phone == phone:
                return user
        raise ValueError("Пользователь не найден")

    def get_id(self):
        return self.id

    def set_phone(self, phone):
        pass
