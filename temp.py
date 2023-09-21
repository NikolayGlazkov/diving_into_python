import csv

def get_max_id():
    max_id = 0
    with open('phone_book.csv', 'r', newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
        for row in data:
            try:
                row_id = int(row[0])
                if row_id > max_id:
                    max_id = row_id
            except ValueError:
                pass
    return max_id
current_id = 1

def create_new_member():
    global current_id
    
    array = []
    array.append(str(current_id))
    array.append(input(f"Введите фамилию: ").title())
    array.append(input(f"Введите имя: ").title())
    array.append(input(f"Введите номер: "))
    array.append(input(f"Введите заметку: "))
    current_id += 1
    return array

def write_new_to_file():
    with open('phone_book.csv', 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(create_new_member())

def open_csv():
    with open('phone_book.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
    print("")

def update_member_by_lastname():
    lastname = input("Введите фамилию пользователя для обновления: ")
    found = False
    updated_data = create_new_member()
    
    with open('phone_book.csv', 'r', newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
        
    for i, row in enumerate(data):
        if row[1] == lastname:
            data[i] = updated_data
            found = True
    
    if found:
        with open('phone_book.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerows(data)
        print("Данные пользователя обновлены.")
    else:
        print("Пользователь с указанной фамилией не найден.")

def delete_member_by_lastname():
    lastname = input("Введите фамилию пользователя для удаления: ")
    found = False
    
    with open('phone_book.csv', 'r', newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
    
    for i, row in enumerate(data):
        if row[1] == lastname:
            del data[i]
            found = True
    
    if found:
        with open('phone_book.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerows(data)
        print("Пользователь удален.")
    else:
        print("Пользователь с указанной фамилией не найден.")

def menu():
    while True:
        print("Выберите действие:")
        print("1. Создать новую запись")
        print("2. Чтение справочника")
        print("3. Обновить данные пользователя в справочнике")
        print("4. Удалить пользователя по фамилии")
        print("5. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            write_new_to_file()
            print("Запись успешно создана и сохранена в справочнике.")
        elif choice == "2":
            open_csv()
        elif choice == "3":
            update_member_by_lastname()
        elif choice == "4":
            delete_member_by_lastname()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

menu()
