# class Singleton:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#     def __init__(self, name: str):
#         self.name = name
# a = Singleton('Первый')
# print(f'{a.name = }')
# b = Singleton('Второй')
# print(f'{a is b = }')
# print(f'{a.name = }\n{b.name = }')

# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра
class Archive():
   def __new__(self, value, name): #__new__ принимает три аргумента: cls (класс), value (значение числа), и name (имя числа).
        #  __new__ является статическим методом, 
        # который используется для создания нового экземпляра класса. 
        # Обычно он вызывается перед __init__
        instance = super().__new__(cls, value) #вызывает __new__ родительского класса int, создавая экземпляр числового типа с заданным значением value.
        super().__new__(cls, value) 
        instance.name = name
        return instance
