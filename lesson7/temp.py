from datetime import datetime

# Режим	Обозначение
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись

# with open("myfile.txt", "r+",encoding="utf-8") as my_file:
  
#   file_contents = my_file.read()
#   my_file.close()
# print(file_contents)

get_date = lambda d: datetime.strptime(d, '%d.%m.%Y').date() <= datetime.today().date()
assert get_date('14.09.2019')  # OK
print(get_date('12.09.2019'))  # AssertionError
# assert get_date('32.09.2019')  # ValueError: time data '32.09.2019' does not match format '%d.%m.%Y'