# Напишите программу, которая принимает две строки вида “a/b” - 
# дробь с числителем и знаменателем. Программа должна возвращать 
# сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
from math import gcd
# print(Fraction(numerator=1, denominator=4)+Fraction(numerator=2, denominator=5))

def menu(my_str,my_str1):
    while True:
        print("Выбирите одно из действий :")
        print("1 - сложение дробей")        
        print("2 - умножение")
        print("3 - выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            print(sum_of_fractions(my_str,my_str1))
            print("Option1 colded")
            print()
        elif choice == "2":
            print(umn_of_fractions(my_str,my_str1))
            print("Option2 colded")
            print()
        elif choice == "3":
            break 
        else:
            print("Неверный выбор. Попробуйте снова.")


def umn_of_fractions(my_str,my_str1):
    n_1, d_1 = map(int,my_str.split("/"))
    n_2, d_2 = map(int,my_str1.split("/"))
    return f"{n_1 * n_2}/{d_1 * d_2}"

def sum_of_fractions(my_str,my_str1):
    n_1, d_1 = map(int,my_str.split("/")) # d1 знаменатель первой дроби
    n_2, d_2 = map(int,my_str1.split("/")) # d2 знаменатель второй дроби
    if d_1 == d_2:
        return f"{n_1+n_2}, {d_2}" # если знаменатель равный выводим сумму числителя и знаменатель внизу
    else:
        cd = int(d_1*d_2/gcd(d_1, d_2))
        rn = int(cd/d_1*n_1+cd/d_2*n_2)
        g2 = gcd(rn, cd) # наибольшый общий делитель
        n = int(rn/g2)
        d = int(cd/g2)
        return f'{n}/{d}' if n != d else n
        
frac1 = input("введите первое число : ")
frac2 = input("введите второе число : ")
menu(frac1,frac2)       

