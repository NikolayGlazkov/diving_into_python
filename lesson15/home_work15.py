"""Я так и не понял откуда брать задачи для которых надо добавить логирование
поэтому возьму задачу с степика) Я ее довно ершил условие:
Во время решения очередной задачи программист фиксирует время начала и окончания 
ее решения и добавляет полученные результаты в список data. Каждый результат 
представляет собой кортеж, первым элементом которого является время начала решения 
в виде строки в формате HH:MM, вторым элементом — время окончания решения в 
виде строки в том же формате. Дополните приведенный ниже код, чтобы он вывел 
общее целое количество минут, которое программист затратил на решение всех задач."""

import argparse
import logging
from datetime import datetime, timedelta

def calculate_total_time(data):
    total_time = timedelta()
    for start_time, end_time in data:
        try:
            start_datetime = datetime.strptime(start_time, "%H:%M")
            end_datetime = datetime.strptime(end_time, "%H:%M")
            time_diff = end_datetime - start_datetime
            total_time += time_diff
        except ValueError as e:
            logging.error(f"Ошибка при обработке времени: {e}")
    return total_time

def main():
    parser = argparse.ArgumentParser(description='Вычисление общего времени на решение задач.')
    parser.add_argument('file_path', type=str, help='Путь к файлу с данными задач')

    args = parser.parse_args()

    try:
        with open(args.file_path, 'r') as file:
            data = [line.strip().split() for line in file.readlines()]
    except FileNotFoundError:
        logging.error(f"Файл не найден: {args.file_path}")
        return
    except Exception as e:
        logging.error(f"Ошибка при чтении файла: {e}")
        return

    total_time = calculate_total_time(data)
    print(f"Общее время на решение задач: {int(total_time.total_seconds() / 60)} минут")

if __name__ == "__main__":
    logging.basicConfig(filename='logfile.log', level=logging.ERROR)
    main()
