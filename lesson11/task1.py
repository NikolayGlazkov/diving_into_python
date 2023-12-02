import time

class NamedInt(int):
    def __new__(cls, value, name): #__new__ принимает три аргумента: cls (класс), value (значение числа), и name (имя числа).
        #  __new__ является статическим методом, 
        # который используется для создания нового экземпляра класса. 
        # Обычно он вызывается перед __init__
        instance = super().__new__(cls, value) #вызывает __new__ родительского класса int, создавая экземпляр числового типа с заданным значением value.
        super().__new__(cls, value) 
        instance.name = name
        return instance
    
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
class MyStr(str):
    def __new__(cls, value, author_name):
        instance = super(MyStr, cls).__new__(cls, value)
        instance.creation_time = time.time()
        instance.author = author_name
        return instance
        
    
author_name = "John Doe"
my_string = MyStr("Hello, World!", author_name)
print(my_string)  # Вывод строки
print(my_string.creation_time)  # Вывод времени создания
print(my_string.author)  # Вывод автора