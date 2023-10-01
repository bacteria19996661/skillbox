#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Часть 2. Модуль 13. Практическая работа. Задача 2. Пути файлов
#
# Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам
# указанной директории (по умолчанию — корневой диск), находит указанный пользователем
# каталог и генерирует пути всех встреченных файлов. В решении не нужно использовать рекурсию.
#
# Подсказка: вместо написания кода с рекурсией используйте готовую рекурсивную функцию
# os.walk() — os — Miscellaneous operating system interfaces — Python 3.11.0 documentation.
#
# Что оценивается
# Результат вычислений корректен.
# Сообщения о процессе получения результата осмыслены и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs).
# Если функция/метод ничего не возвращает, то используется None.

import os


def gen_files_path(some_dir):
    # рекурсивно проходит по всем каталогам указанной директории (по умолчанию — корневой диск)
    try:
        for root, dirs, files in os.walk(some_dir, onerror=None):
            # находит указанный пользователем каталог
            # если встречается файл, генерирует его абсолютный путь
            for i_file in files:
                print(i_file)
    except KeyboardInterrupt as e1:
        print(type(e1))
    except UnicodeEncodeError as e2:
        print(type(e2))
    except PermissionError as e3:
        print(type(e3))


if __name__ == '__main__':
    path_to = input('Введите полный путь к каталогу: ')

    if path_to:
        if os.path.isabs(path_to):
            if os.path.isdir(path_to):
                gen_files_path(path_to)
            elif os.path.isfile(path_to):
                print("Это файл!")
        else:
            raise Exception('Вы ввели что-то не то!')
    else:
        gen_files_path(os.path.abspath(os.path.join(os.sep)))
