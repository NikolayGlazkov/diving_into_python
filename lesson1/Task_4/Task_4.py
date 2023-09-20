# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
from random import randint

num = randint(0, 1001)
print(num)
counter = 0
while True:
    ans_num = int(input(f"угадайте что я загадал?"))
    if ans_num == num:
        print("вы угодали"),True
        break
    if ans_num < num:
        print(f"загаданное число больше {ans_num}")
    if ans_num > num:
        print(f"загаданное число меньше {ans_num}")
    counter +=1

print(f'вам понадобилось {counter} попыток')