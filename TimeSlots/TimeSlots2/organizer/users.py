import time

sec = time.time()
print("Местное время:", sec)
local_time = time.ctime(sec)
print("Местное время:", local_time)
named_tuple = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print(time_string)

widgets = {
    'field_user_surname': TextInput(attrs={
        'class': "form-control",
        'id': "field_user_surname",
        'aria-describedby': "field_user_surnameHelp",
        'lenght': 50
    })
    'field_user_name': TextInput(attrs={
        'class': "form-control",
        'id': "field_user_name",
        'aria-describedby': "field_user_nameHelp",
        'lenght': 50
    })
    'field_user_name2': TextInput(attrs={
        'class': "form-control",
        'id': "field_user_name2",
        'aria-describedby': "field_user_name2Help",
        'lenght': 50
    })
    'field_user_position': TextInput(attrs={
        'class': "form-control",
        'id': "field_user_position",
        'aria-describedby': "field_user_positionHelp",
        'lenght': 50
    })
    'field_user_org_name': TextInput(attrs={
        'class': "form-control",
        'id': "field_user_org_name",
        'aria-describedby': "field_user_org_nameHelp",
        'lenght': 50
    })
    'field_user_city': TextInput(attrs={
        'class': "form-control",
        'id': "field_user_city",
        'aria-describedby': "field_user_cityHelp",
        'lenght': 50
    })
    'field_user_street': TextInput(attrs={
        'class': "form-control",
        'id': "field_user_street",
        'aria-describedby': "field_user_streetHelp",
        'lenght': 50
    })
    'field_user_hauce': TextInput(attrs={
        'class': "form-control",
        'id': "field_user_hauce",
        'aria-describedby': "field_user_hauceHelp",
        'lenght': 50
    })
    'field_user_phone': TextInput(attrs={
        'class': "form-control",
        'id': "field_user_phone",
        'aria-describedby': "field_user_phoneHelp",
        'lenght': 50
    })
    'field_user_email': TextInput(attrs={
        'class': "form-control",
        'id': "field_user_email",
        'aria-describedby': "field_user_emailHelp",
        'lenght': 50
    })
}

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
    def __init__(self, name, surname, phone, service_type):
        super().__init__(name, surname, phone)
        self.service_type = service_type
        self.__id = self.get_id()

    def __str__(self):
        return str(self.__id) + ' ' + str(self.name) + ' ' + str(self.surname) + ' ' + str(self.phone) + ' ' + str(self.service_type)

class ServiceObject(object):
    __last_id = 0
    __list = dict()
    def __init__(self, name, service_type, status):
        ServiceObject.__last_id += 1
        self.id = ServiceObject.__last_id
        self.name = name
        self.service_type = service_type
        self.status = status

    def set_customer(self, customer):
        self.customer = customer

    def set_implementers(self, implementers):
        self.implementers = implementers

    def __str__(self):
        return str(self.id) + ' ' + str(self.name) + ' ' + str(self.service_type) + ' ' + str(self.status)

class Order(object):
    __last_id = 0
    __list = dict()
    def __init__(self, implementer, service_object, service_type, status, description):
        Order.__last_id += 1
        self.id = Order.__last_id
        self.implementer = implementer
        self.service_object = service_object
        self.service_type = service_type
        self.status = status
        self.description = description

    def __str__(self):
        return str(self.id) + ' ' + str(self.implementer.surname) + ' ' + str(self.service_object.name) + ' ' + \
               str(self.service_type) + ' ' + str(self.status) + ' ' + str(self.description)


customer1 = Customer('Михаил', 'Недялко', '+79112321654', ('video', 'sked', 'signalka', 'pozharka', 'domofon'))
implementer1 = Implementer('Юлия', 'Недялко', '+79118101354', ('video', 'sked'))
service_object_1 = ServiceObject('ООО ФЕРМЕР-МАРКЕТ', ('video', 'skud'), 'status1')
service_object_1.set_customer(customer1)
service_object_1.set_implementers(implementer1)
order1 = Order(implementer1, service_object_1, ('video'), 'заявка', 'нужны дополнительные камеры')


print(str(customer1))
print(implementer1)
print(service_object_1)
print(str(service_object_1) + ' ' + str(service_object_1.customer) + ' ' + str(service_object_1.implementers))
print(order1)