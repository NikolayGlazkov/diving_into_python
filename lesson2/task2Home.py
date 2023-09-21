# Напишите программу, которая получает целое число и возвращает 
# его шестнадцатеричное строковое представление. Функцию hex используйте для проверки 
# своего результата.


num = 1613 #int(input()) # ввод числа
#можно используя f-строки и формат вывода. Для этого в строке, через символ ":"" указываем буквы 
# b – для двоичной,
# o – для восьмеричной и 
# x – для шестнадцатеричной системы счисления.
print(f'Двоичное: {num:b}')
print(f'Восьмеричное: {num:o}')
print(f'Шестнадцатеричное: {num:x}')
print("")

def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

digit = int(input("Введите число :"))
sist = int(input("Введите систему исчесления :"))
print(f"перевод в {sist} систему исчесления равен: {convert_to(digit,sist)}")