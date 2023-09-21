# Напишите программу, которая принимает две строки вида “a/b” - 
# дробь с числителем и знаменателем. Программа должна возвращать 
# сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
from math import gcd
print(Fraction(numerator=1, denominator=4)+Fraction(numerator=2, denominator=5))

#“a/b”

def sum_of_fractions(my_str,my_str1):
    n_1, d_1 = map(int,my_str.split("/"))
    n_2, d_2 = map(int,my_str1.split("/"))
    if d_1 == d_2:
        return f"{n_1+n_2}, {d_2}"
    else:
        cd = int(d_1*d_2/gcd(d_1, d_2))
        rn = int(cd/d_1*n_1+cd/d_2*n_2)
        g2 = gcd(rn, cd)
        n = int(rn/g2)
        d = int(cd/g2)
        return f'{n}/{d}' if n != d else n



frac1 = input("введите первое число : ")
frac2 = input("введите второе число : ")
print(sum_of_fractions(frac1,frac1))

# код недописан начну писать про банкомат потом сюда вернусь