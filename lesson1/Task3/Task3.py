# 3. Напишите код, который запрашивает число и сообщает является ли оно простым 
# или составным. Используйте правило для проверки: “Число является простым, 
# если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def isPrime(dig):
    if dig < 2 or dig > 100_000:
        return "Введите число от 2 до 100000"
    
    counter = 0  # счетчик количества делителей
    for i in range(2, int(dig ** 0.5) + 1):
        if dig % i == 0:
            counter += 1

    if counter == 0:
        return f"Число {dig} простое"
    else:
        return f"Число {dig} составное"

try:
    num = int(input("Введите число: "))
    result = isPrime(num)
    print(result)
except ValueError:
    print("Введите корректное целое число")