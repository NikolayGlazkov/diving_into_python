"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст."""


class UserInfo:
    def __init__(self,name,lastname,otchestvo,age):
        self.name = name
        self.lastname = lastname
        self.otchestvo = otchestvo
        self.__age = age
    def birthday(self):
        self.__age +=1
    def full_name (self):
        return f"{self.name} {self.lastname} {self.otchestvo}"
    def get_age(self):
        return self.__age
    
user = UserInfo("Иван","Иванов","Иванович",99)

user.birthday()
print(user.get_age())
print(user.full_name())