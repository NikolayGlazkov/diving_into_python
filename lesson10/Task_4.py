"""
Создайте класс Сотрудник.
📌 Воспользуйтесь классом человека из прошлого задания.
📌 У сотрудника должен быть:
    ○ шестизначный идентификационный номер
    ○ уровень доступа вычисляемый как остаток от деления
      суммы цифр id на семь
"""

from Task_3 import UserInfo
import random
class Emploer(UserInfo):
    def __init__(self,name,lastname,otchestvo,age,id_number):
        super().__init__(name,lastname,otchestvo,age)
        if len(str(id_number)) != 6:
            self.id_number = random.randint(100_000,999_999)
        else:
            self.id_number = id_number

    def secure_level(self):
        return sum ([int(i) for i in str(self.id_number)])
    
user = ("Иван","Иванов","Иванович",99,123445)
print(user)