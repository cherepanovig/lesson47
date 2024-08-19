# Домашнее задание по теме "Многопроцессное программирование"
# Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.

#import time
from datetime import datetime
import multiprocessing


def read_info(name_f):
    all_data = []
    with open(name_f, 'r', encoding='utf-8') as file:  # Открываем каждый файл на чтение
        while True:  # пока считанная строка существует
            line = file.readline()  # читаем файл построчно
            if not line:  # если строки нет то прерываем чтение файла
                break
            all_data.append(line)  # добавляем строки в список
    #return all_data


filenames = [f'./files/file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    # Линейный вызов
    time_start = datetime.now()
    for name_f in filenames:  # перебираем все мена файлов в списке [filenames]
        read_info(name_f)  # передаем в качестве аргумента функции read_info название файла
    time_end = datetime.now()
    print(f'Время выполнения (линейный способ): {time_end - time_start} сек')

    # Многопроцессный вызов
    #if __name__ == '__main__':
    time_start = datetime.now()
    with multiprocessing.Pool() as pool:  # Создается пул процессов
        pool.map(read_info, filenames)  # map примен-ся для параллельного вызова функции read_info для каждого файла
    time_end = datetime.now()
    print(f'Время выполнения (многопроцессорный способ): {time_end - time_start} сек')
