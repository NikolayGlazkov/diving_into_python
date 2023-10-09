import random
import os
import sys


def make_rand_file_ext(): # количество раз создания файлов
    extension = ["txt","png","jpg","pdf"]
    my_str = "The movie is set in modern England and in a fictional place called Hogwarts. The story is a mixture of real-life drama and fantasy. The main character of the movie is a ten-year-old orphan Harry. His parents died when he was a baby, and now he lives with his foster parents and his stepbrother who do not like him. Although Harry has a family, he is a very lonely boy.What I like about this movie is how drastically Harry’s life changed one day. On his eleventh birthday he was invited to study at Hogwarts, the magic school that, as it turned out, his parents had attended. He started learning how to use magic and fly on a broomstick. He found good friends and a new home. At the beginning of the movie, Harry is just an ordinary boy. At the end of the movie, he is a hero and one of the most promising young wizards in Hogwarts."
    array_of_name = my_str.split(" ")
    answer =  f'{random.choice(array_of_name)}.{random.choice(extension)}'
    return answer

def random_make_file(num:int):
    for i in range(num):
        my_file = open(make_rand_file_ext(), "w")
        my_file.close()

num = int(input('сколько раз запускать: '))

random_make_file(num+1) # это пришлось сделать чтоб было с чем работать


# Напишите функцию группового переименования файлов.

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


# def reneim_of_file(
#     new_name: str, ferst_ext: str, new_ext: str, kol: int
# ):  # new_name - новое имя

    # os.rename()

def rename_some_file(new_name,new_ext,ferst_ext,kol,ferst_name_dip):
    array_of_file = os.listdir()
    temp_rray = []
        # print(array_of_file)
    for file in array_of_file:
        if file.split(".")[-1] == ferst_ext:
            temp_rray.append(file)
    count = 0
    for file in temp_rray[:kol]:
        os.rename(file, f"{file.split()[0][:ferst_name_dip]}_{new_name}_{count}.{new_ext}")
        count += 1
    print("Скрипт выполнен")


new_name = input("Введите новое имя файлов: ")
new_ext = input("Введите новое расширение файов: ")
ferst_ext = input("Введите новое расширение: ")
kol = int(input("Введите количчество файлов: "))
ferst_name_dip = int(input("введите сколько букв от старого имени будем использовать в начале"))

rename_some_file(new_name,new_ext,ferst_ext,kol,ferst_name_dip)