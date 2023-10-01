#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 13. Практическая работа. Задача 5. Обработка логов
#
# Задача
# Напишите программу, которая считывает строки из файла и выводит строки, содержащие слово ERROR, в новый файл.
#
# Требования
# Используйте модуль os для работы с файлами и путями.
# Учтите, что файл может быть очень большим по объёму, поэтому не загружайте его в память целиком.
# Создайте функцию-генератор error_log_generator, которая будет получать на вход путь до файла с логами
# и возвращать строки из этого файла, которые содержат слово ERROR (одно обращение к генератору должно
# возвращать одну строку из файла).
#
# Советы
# Цикл for по файлу будет считывать в память ровно по одной строке из файла за итерацию.
# Генератор должен возвращать только строки со словом ERROR. Другие строки, которые будут
# считываться из файла, нужно будет игнорировать (применять yield только к правильным строкам).
# Для наглядного примера вы можете сгенерировать очень большой текстовый файл
# (для этого надо запустить код из файла text_generator.py) и попробовать загрузить
# его в память при помощи метода read(), применённого к этому файлу.
# Учтите, что генерация файла такого размера может занять несколько десятков минут!

import os
# import random
# import string
#
# def create_log():
#     path = os.path.join('log.txt')
#     abs_path = os.path.abspath(path)
#     with open(abs_path, 'w', encoding='utf-8') as file:
#         for _ in range(10**1000):
#             some_lst = [random.choice(string.ascii_lowercase) for _ in range(random.randint(10, 100))]
#             some_str = ''.join(some_lst)
#             key = random.randint(1,4)
#             if key == 3:
#                 my_str = ' '.join(('ERROR', some_str, '\n'))
#                 file.write(my_str)
#             else:
#                 file.write(some_str+'\n')
#
# create_log()


def error_log_generator(path_to_file):
    path = os.path.join(path_to_file)
    abs_path = os.path.abspath(path)
    with open(abs_path) as file:
        for line in file:
            if 'ERROR' in line:
                yield line


def error_log_list(max_words=100000):
    with open('log_err.txt', 'a+', encoding='utf-8') as file_err:
        err_gen = error_log_generator('log.txt')

        file_err.seek(0, 0)  # Goes to the begining of the file
        line_count = len(file_err.readlines())   # Counts how many lines the file has

        for i in range(line_count, max_words):
            file_err.write(next(err_gen))    # Writes the next line in the sequence


error_log_list()
