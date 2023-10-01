import decimal



def deposit_cash():
    pass

def withdraw_cash():
    pass
def shou_balance(num):
        return decimal.Decimal(num),

# def menu():
#     print("Выбирите одно из действий :")
#     print("1 - внести наличные")        
#     print("2 - снять наличные")
#     print("3 - посмотреть баланс")
#     print("4 - выход")









balance =  45544

def menu():
    while True:
        print("Выбирите одно из действий :")
        print("1 - внести наличные")        
        print("2 - снять наличные")
        print("3 - посмотреть баланс")
        print("4 - выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            #deposit_cash()
            print("Option1 colded")
        elif choice == "2":
            #withdraw_cash()
            print("Option2 colded")
        elif choice == "3":
            print(f"На вашем считу :")
            print(*shou_balance(balance),"руб.")
        elif choice == "4":
            break 
        else:
            print("Неверный выбор. Попробуйте снова.")

def pin_code():
    chances = 3
    while chances > 0:
        pasword = int(input("enter the pasword"))
        if pasword == 1234:
            menu()
        else:
            chances -=1
            print("У вас осталось {chances} попыток")


pin_code()