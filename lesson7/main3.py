# Напишите функцию, которая открывает
# на чтение созданные в прошлых задачах
# файлы с числами и именами. Перемножьте пары чисел.

# В новый файл сохраните имя и произведение:
#   если результат умножения отрицательный,
#   сохраните имя записанное строчными буквами и произведение по модулю

#   если результат умножения положительный,
#   сохраните имя прописными буквами и произведение округлённое до целого.

# В результирующем файле должно быть столько же строк,
# сколько в более длинном файле. При достижении конца
# более короткого файла, возвращайтесь в его начало.

def func(path_numbers: str, path_name: str, path_result: str):
    with (
        open(path_numbers, 'r', encoding='utf-8') as data_numbers,
        open(path_name, 'r', encoding='utf-8') as data_name,
        open(path_result, 'a', encoding='utf-8') as data_result
    ):
        len_numbers = sum(1 for _ in data_numbers)
        len_data_name = sum(1 for _ in data_name)

        for i in range(max(len_numbers, len_data_name)):
            num = proc(data_numbers)
            name = proc(data_name)
            num_i, num_f = num.split('|')
            mult = int(num_i) * float(num_f)
            if mult < 0:
                data_result.write(f'{name.lower()} {-mult}\n')
            if mult > 0:
                data_result.write(f'{name.upper()} {mult: .0f}\n')


def proc(name_file):
    text = name_file.readline()
    if text == '':
        name_file.seek(0)
        text = name_file.readline()
    return text.strip()


func('text.txt', 'text_name.txt', 'text_result.txt')