import random as rd
from sys import argv

# Улучшаем задачу 2. Добавьте возможность запуска
# функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов:
# параметры вызова функции. Для преобразования строковых
# аргументов командной строки в числовые
# параметры используйте генераторное выражени

def func(a=1, b=10, c=3):
    num = rd.randint(a, b)
    for attempt in range(c):
        guess = int(input(f"Попытка №{attempt + 1}: "))
        if guess < num:
            print("Загаданное число больше.")
        elif guess > num:
            print("Загаданное число меньше.")
        else:
            print("Поздравляю! Вы угадали число!")
            return True

    print("Вы исчерпали все попытки. Загаданное число было:", num)
    return False


if __name__ == '__main__':
    # temp = [int(i) for i in argv[1::]]
    print(func(*[int(i) for i in argv[1::]]))
    print(func(*argv))