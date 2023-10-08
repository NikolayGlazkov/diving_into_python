
# Напишите функцию группового переименования файлов. 
#Она должна:
#  - принимать параметр желаемое конечное имя файлов. 
#  - При переименовании в конце имени добавляется порядковый номер.
#  - принимать параметр количество цифр в порядковом номере?????.
#  - принимать параметр расширение исходного файла. 
#  - Переименование должно работать только для этих файлов внутри каталога.
#  - принимать параметр расширение конечного файла.
#  - принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. name = temp.txt
# К ним прибавляется желаемое конечное имя, если оно передано. 
# Далее счётчик файлов и расширение. tem_items_num.pdf

#Соберите из созданных на уроке и в рамках домашнего задания 
# функций пакет для работы с файлами.
import random
import os

def make_rand_file(num:int): # количество раз создания файлов
    extension = ["txt","png","jpg","pdf"]
    for i in range(num):
        print(random.choice(extension))

# make_rand_file(3)


# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.


# def num_of_dev(file: str,count: int):
#     glas = 'eyuioa'
#     sagl =  'qwrtpsdfghjklzxcvbnm'
    
#     with open(file, 'a', encoding='utf-8') as data:
#         for j in range(count):
#             num_it = random.randint(4,7)
#             answer = []
#             for i in range(7):
#                 answer.extend([random.choice(glas),random.choice(sagl)])
#             print("".join(answer).title()[:num_it],file=data)

            
# if __name__ == '__main__':
#     num_of_dev('text.txt',5)

# my_file = open("BabyFile.txt", "w+")
# my_file.write("Привет, файл!")
# my_file.close()

print()
print("Текущая деректория:",os.getcwd()) 
# # if not os.path.isdir("lesson_7_for_temp_file"):
# os.mkdir("lesson_7_for_temp_file",mode=0o777,dir_fd=None)

# print(os.path.isdir())

dir_name = 'lesson_7_for_temp_file'

# print('Creating', dir_name) # иноформация для консоли
# os.makedirs(dir_name) # создание дериктории

file_name = os.path.join(dir_name, 'example.txt')
print('Creating', file_name) # имя файла это второй аргумент из списка
with open(file_name, 'wt') as f:
    f.write('example file')

print('Cleaning up')
os.unlink(file_name)
os.rmdir(dir_name)
