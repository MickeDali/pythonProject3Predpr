from django.db import models
import time

sec = time.time()

# Create your models here.
class Task(models.Model):
    title = models.CharField('Title', max_length=180)               # заголовок
    description = models.TextField('Description', max_length=256)
    time_create = time.localtime()
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


class Address(object):
    def __init__(self, location, city, street, dom, korpus, liter, index, phones, contacts, email):
        pass


class Customer(User):
    def __init__(self, name, surname, phone, service_type):
        super().__init__(name, surname, phone)
        self.service_type = service_type
        self.__id = self.get_id()

    def __str__(self):
        return str(self.__id) + ' ' + str(self.name) + ' ' + str(self.surname) + ' ' + str(self.phone) + ' ' + str(self.service_type)


class Implementer(User):
    def __init__(self, name, surname, phone, service_type, service_objects_list, title, description, mobile, type_of_work, type_of_system, qualification ):
        super().__init__(name, surname, phone)
        self.__id = self.get_id()
        self.rating                             # рейтинг
        self.title = title                      # профессия
        self.description = description          # резюме
        self.mobile = mobile                    # мобильность (общественный транспорт, личный авто)
        self.type_of_work = type_of_work        # специализация по типу работ (монтаж, ремонт, обслуживание, поддержка)
        self.type_of_system = type_of_system    #   -тип специализация по типу системы (Видео, СКУД, домофон, электрика, пожарка, тв, интернет, сети)
        self.qualification  = qualification     # квалификация (стажер, обучен)
        # календарь заявок
        # расписание
        # список объектов
        # список заказчиков
        # история
        # хранилище данных (фото, видео, схемы, файлы)
        # геоданные (расположение, охват, маршруты)
        #

    def __str__(self):
        return str(self.__id) + ' ' + str(self.name) + ' ' + str(self.surname) + ' ' + str(self.phone) + ' ' + str(self.service_type)

class ServiceObject(object):
    __last_id = 0
    __list = dict()
    def __init__(self, name, title, service_type, status):
        ServiceObject.__last_id += 1
        self.id = ServiceObject.__last_id
        self.name = name                    # Название объекта
        self.title = title                  # Полное наименование объекта
        self.service_type = service_type    # тип сервиса (Видео, СКУД, домофон, электрика, пожарка, тв, интернет, сети)
        self.status = status                # статус (норма, заявка на обслуживание, ожидание обслуживания, обслуживание, обслуживание прошел)
        self.
        # геоданные GPS, карта с положением
        # альбомы (схемы, фото, видео, файлы, записи)
        # список исполнмиелей с рейтингом
        # история обслуживания
        # календарь заявок
        #
        # метод добавления геоданных

    def set_customer(self, customer):
        self.customer = customer

    def set_implementers(self, implementers):
        self.implementers = implementers

    def __str__(self):
        return str(self.id) + ' ' + str(self.name) + ' ' + str(self.service_type) + ' ' + str(self.status)

class Order(object):
    __last_id = 0
    __list = dict()
    def __init__(self, desired_implementer, implementer, service_object, service_type, status, description, time_create, desired_execution_time ):
        Order.__last_id += 1
        self.id = Order.__last_id
        self.desired_implementer = desired_implementer  # предпологаемый исполнитель
        self.implementer = implementer          # фактический  исполнитель
        self.service_object = service_object    # обслуживаемый объект
        self.service_type = service_type        # тип объекта
        self.status = status                    # статус заявки
        self.description = description          # описание заявки
        self.time_create = time_create          # время подачи заявки
        self.desired_execution_time = desired_execution_time    # желаемое время иссполнения
        # фото

    def __str__(self):
        return str(self.id) + ' ' + str(self.implementer.surname) + ' ' + str(self.service_object.name) + ' ' + \
               str(self.service_type) + ' ' + str(self.status) + ' ' + str(self.description)


# customer1 = Customer('Михаил', 'Недялко', '+79112321654', ('video', 'sked', 'signalka', 'pozharka', 'domofon'))
# implementer1 = Implementer('Юлия', 'Недялко', '+79118101354', ('video', 'sked'))
# service_object_1 = ServiceObject('ООО ФЕРМЕР-МАРКЕТ', ('video', 'skud'), 'status1')
# service_object_1.set_customer(customer1)
# service_object_1.set_implementers(implementer1)
# order1 = Order(implementer1, service_object_1, ('video'), 'заявка', 'нужны дополнительные камеры')
#
#
# print(str(customer1))
# print(implementer1)
# print(service_object_1)
# print(str(service_object_1) + ' ' + str(service_object_1.customer) + ' ' + str(service_object_1.implementers))
# print(order1)
