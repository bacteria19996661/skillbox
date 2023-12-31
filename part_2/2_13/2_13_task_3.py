#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 13. Практическая работа. Задача 3. Количество строк
#
# Реализуйте функцию-генератор, которая берёт все питоновские файлы в
# директории и вычисляет количество строк в каждом файле, игнорируя пустые строки
# и строки комментариев. По итогу функция-генератор должна с помощью yield каждый
# раз возвращать количество строк в очередном файле.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Сообщения о процессе получения результата осмыслены и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs).
# Если функция/метод ничего не возвращает, то используется None.

from pathlib import Path


def find_py(cur_path):
    paths = sorted(Path(cur_path).glob('**/*.py'))
    paths_list = list(map(str, paths))     # преобразовать в список строк
    paths_list_count = []
    for el in paths_list:
        try:
            with open(el) as file:
                count = 0
                for line in file:
                    if line.strip() and line[0] != '#':
                        count += 1
                paths_list_count.append((el, count))
        except UnicodeDecodeError as e1:
            print(e1, type(e1))
    yield paths_list_count


if __name__ == '__main__':
    usr_path = input('Введите путь: ')
    for el in find_py(usr_path):
        print(el)
