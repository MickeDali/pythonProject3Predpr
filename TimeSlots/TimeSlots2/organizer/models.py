from django.db import models
import time

sec = time.time()

__last_id = 0

# Create your models here.
class Task(models.Model):
    title = models.CharField('Title', max_length=180)               # заголовок
    description = models.TextField('Description', max_length=256)
    #time_create = time.localtime()
    #time_start = time.localtime()
    #time_stop = time.localtime()

    def str(self):
        return self.title

class User(models.Model):
    class Meta:


    __list = dict()
    __last_id += 1
    id = __last_id

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
    class Meta:
        db_table = "Customer"
    #__id = get_id()
    surname = models.CharField('customer_surname', max_length=20, help_text="Введите фамилию")
    name = models.CharField('customer_name', max_length=20, help_text="Введите имя")
    phone = models.CharField('customer_phone', max_length=20, help_text="Введите номер телефона")
    service_type = models.CharField('service_type', max_length=180)
    service_objects_list = models.CharField('service_objects_list', max_length=180)

    #def __str__(self):
    #    return str(self.__id) + ' ' + str(self.name) + ' ' + str(self.surname) + ' ' + str(self.phone) + ' ' + str(self.service_type)


class Implementer(User):
    class Meta:
        db_table = "Implementer"
    #__id = get_id()
    rating = models.CharField('rating', max_length=180)                    # рейтинг
    title = models.CharField('title', max_length=180)                      # профессия
    description = models.CharField('description', max_length=180)          # резюме
    mobile = models.CharField('mobile', max_length=180)                    # мобильность (общественный транспорт, личный авто)
    type_of_work = models.CharField('type_of_work', max_length=180)        # специализация по типу работ (монтаж, ремонт, обслуживание, поддержка)
    type_of_system = models.CharField('type_of_system', max_length=180)    #   -тип специализация по типу системы (Видео, СКУД, домофон, электрика, пожарка, тв, интернет, сети)
    qualification  = models.CharField('qualification', max_length=180)     # квалификация (стажер, обучен)
    calendar_order = models.CharField('calendar_order', max_length=180)    # календарь заявок, расписание
    objects_list = models.CharField('objects_list', max_length=180)        # список объектов
    customers_list = models.CharField('customers_list', max_length=180)    # список заказчиков
        # история
        # хранилище данных (фото, видео, схемы, файлы)
        # геоданные (расположение, охват, маршруты)
        #

    #def __str__(self):
    #    return str(self.__id) + ' ' + str(self.name) + ' ' + str(self.surname) + ' ' + str(self.phone) + ' ' + str(self.service_type)

class ServiceObject(models.Model):
    __last_id = 0
    __list = dict()
    __last_id += 1
    id = __last_id
    name = models.CharField('name', max_length=180)                # Название объекта
    title = models.CharField('title', max_length=180)               # Полное наименование объекта
    service_type = models.CharField('service_type', max_length=180)        # тип сервиса (Видео, СКУД, домофон, электрика, пожарка, тв, интернет, сети)
    status = models.CharField('status', max_length=180)              # статус (норма, заявка на обслуживание, ожидание обслуживания, обслуживание, обслуживание прошел)
    implementers_list = models.CharField('implementers_list', max_length=180)   # список исполнмиелей с рейтингом
    client = models.CharField('client', max_length=180)
    #self.client = SearchClient('aa51fbe7-81ec-4ccb-a18c-7bd47bf08302')
    #client.search('Санкт-Петербург, ул. Тихоокеанская, 14 корпус 2', lang='ru_RU') # геоданные GPS, карта с положением
        # альбомы (схемы, фото, видео, файлы, записи)
        # история обслуживания
        # календарь заявок
        # метод добавления геоданных

    #def set_customer(self, customer):
    #    self.customer = customer

    #def set_implementers(self, implementers):
    #    self.implementers = implementers

    #def __str__(self):
    #    return str(self.id) + ' ' + str(self.name) + ' ' + str(self.service_type) + ' ' + str(self.status)

class Order(models.Model):
    __last_id = 0
    __list = dict()
    __last_id += 1
    id = __last_id
    desired_implementer = models.CharField('desired_implementer', max_length=180)  # предпологаемый исполнитель
    implementer = models.CharField('implementer', max_length=180)          # фактический  исполнитель
    service_object = models.CharField('service_object', max_length=180)    # обслуживаемый объект
    service_type = models.CharField('service_type', max_length=180)        # тип объекта
    status = models.CharField('status', max_length=180)                    # статус заявки
    description = models.CharField('description', max_length=180)          # описание заявки
    time_create = models.CharField('time_create', max_length=180)          # время подачи заявки
    desired_execution_time = models.CharField('desired_execution_time', max_length=180)    # желаемое время иссполнения
        # фото

    #def __str__(self):
    #    return str(self.id) + ' ' + str(self.implementer.surname) + ' ' + str(self.service_object.name) + ' ' + \
    #           str(self.service_type) + ' ' + str(self.status) + ' ' + str(self.description)


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
