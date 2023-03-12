import time

sec = time.time()
print("Местное время:", sec)
local_time = time.ctime(sec)
print("Местное время:", local_time)
named_tuple = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print(time_string)



class User(object):
    __last_id = 0
    __list = dict()
    def __init__(self, name, surname, phone):
        User.__last_id += 1
        self.id = User.__last_id
        self.name = name
        self.surname = surname
        self.__phone = phone
        self.created = time.time()
        self.last_vizit = self.created
        self.updated = None

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


customer1 = Customer('Михаил', 'Недялко', '+79112321654', ('video', 'sked', 'signalka', 'pozharka', 'domofon'))
implementer1 = Implementer('Юлия', 'Недялко', '+79118101354', ('video', 'sked', 'signalka', 'pozharka', 'domofon'))
print(str(customer1))
print(customer1.service_type)
print(implementer1)
customer1.id = 5
implementer1.id = 6
print(customer1)
print(implementer1)