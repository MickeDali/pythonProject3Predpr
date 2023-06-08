import time

sec = time.time()
print("Местное время:", sec)
local_time = time.ctime(sec)
print("Местное время:", local_time)
named_tuple = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print(time_string)


class TimeSlot(object):

    def __init__(self, time_create, time_start, time_stop, slotslist, status, color, slot_type, text):
        self.time_create = time_create
        self.time_start = time_start
        self.time_stop = time_stop
        self.slotslist = slotslist
        self.status = status
        self.color = color
        self.slot_type = slot_type
        self.text = text

    def set_timeslot(self):
        self.time_start = time_start
        self.time_stop = time_stop
        #slot = list(self.time_start, self.time_stop)
            ##self.status,
            #self.color,
            #self.prioritet,
            #self.slot_type,
            #self.text)
        self.slotslist = slotslist
        self.slotslist.append(self.time_start)
        self.slotslist.append(self.time_stop)
        return self.slotslist

    def get_slotslist(self):
        return slotslist

class TimeLine(object):
    def __init__(self, timeslots):
        pass

    def slot_set(self):
        pass

    def slot_del(self):
        pass

    def slot_move(self):
        pass

class User(object):
    __last_id = 0
    __list = dict()
    def __init__(self, name, surname, phone):
        User.__last_id += 1
        self.id = User.__last_id
        self.name = name
        self.surname = surname
        self.phone = phone
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

    def __str__(self):
        return str(self.id) + str(self.name) + str(self.surname) + str(self.phone)

class Address(object):
    def __init__(self, location, city, street, dom, korpus, liter, index, phones, contacts, email):
        pass

class Shop(object):
    def __init__(self, ):
        pass

class Executor(object):
    def __init__(self):
        pass

class Docs(object):
    def __init__(self, photos, shems, manuals, coments, finanses):
        pass

class Client(object):
    def __init__(self, id, contacts, type, ):
        pass


class Sklad(object):
    def __init__(self, ):
        pass


class  Box_Space(object):
    def __init__(self, time_frame, cobtent):
        pass


class  Box_Part_Day(object):
    def __init__(self, time_frame, parts):
        pass


class  Box_Day(object):
    __slotslist = dict()
    def __init__(self, data_time, day_type):
        self.slotslist = slotslist
        self.data_time = data_time
        self.day_tye = day_type

    def set_timeslot(self):
        pass
    def get_box_day_HTML(self):

        print()


class  Box_Week(object):
    def __init__(self, ):
        pass


class  Box_Month(object):
    def __init__(self, ):
        pass


class  Box_Year(object):
    def __init__(self, ):
        pass


class  Box_Time(object):
    def __init__(self, ):
        pass

#f = open('templates/index.html', 'w')
seconds = time.time()
time_start = time.ctime(seconds)
time_stop = time.ctime(seconds + 600)
timeslot1 = TimeSlot('time_start', 'time_stop', 'slotslist', 'status1', 'red', 'single',  'text1')
slotslist = timeslot1.set_timeslot()

t = (2019, 12, 7, 14, 30, 30, 5, 341, 0)
time_start = time.asctime(t)
print(time_start)
#seconds = time.mktime(time_start)
#print(seconds)
#time_stop = time.ctime(seconds + 600)

timeslot2 = TimeSlot('time_start', 'time_stop', 'slotslist', 'status1', 'red', 'single',  'text1')
slotslist = timeslot2.set_timeslot()
print(slotslist)
print(timeslot1)
