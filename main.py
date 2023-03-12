#from flask import Flask, request, render_template
from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        with tag('p', id = 'main'):
            text('some text')
        with tag('a', href='/my-url'):
            text('some link')

result = doc.getvalue()

class Address(object):
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def __str__(self):
        return self.city + ', ' + self.street

class User(object):
    __count = 0

    def __init__(self, name, surname, age):
        User.__count += 1
        self.__user_id = User.__count
        self.name = name
        self.surname = surname
        self.age = age
        self.__address = None

    def get_user_id(self):
        return self.__user_id

    @staticmethod
    def get_count():
        return User.__count

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if type(address) == Address:
            self.__address = address

    def __str__(self):
        return str(self.__user_id) + ' ' + str(self.name) + ' ' + str(self.surname) + ' ' + str(self.age) + ' ' + str(self.__address)




#f = open('templates/index.html', 'w')
html_template = """

# writing the code into the file
#f.write(html_template)

# close the file
#f.close()


#  создаете ваш экземпляр приложения Flask с именем app
app = Flask(__name__) # переменнуя __name__ содержит имя текущего модуля Python,указывает экземпляру его расположение

@app.route('/')
def index():#variable=None):
    return html_template
    #return render_template('/templates/index.html', variable='12345')

@app.route('/get-text', methods=['GET', 'POST'])
def fo():
    bar = request.form['surname']

if __name__ == '__main__':
    app.run()



address1 = Address('SPb', 'Mira')
user0 = User('М', 'Н', '25')
user1 = User('Михаил', 'Недялко', '42')
#user1 = User(html_template.name, html_template.surname, html_template.age)
user1.address = address1

print(User.get_count())
#print(user1)
#user1.name = input('Name = ')
#user1.surname = input('SurName = ')
#user1.age = input('Age = ')

print(str(user1))

