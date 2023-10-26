#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Часть 2. Модуль 16. Практическая работа. Задача 6. Класс-декоратор
#
# Нужно отслеживать прогресс выполнения алгоритма и анализировать его производительность.
#
# Задача
# Создайте декоратор, который логирует аргументы, результаты и время выполнения функции.
#
# Реализуйте декоратор как класс и примените его к функции complex_algorithm.
# Запустите задекорированную функцию и проверьте время её выполнения.
#
# Замерить время выполнения кода можно при помощи модуля time:
#
# import time
# start_time = time.time() # Записываем время до вычислений
# # ...вычисления...
# end_time = time.time() # Затем записываем время после вычислений
# execution_time = end_time - start_time # Их разница будет временем выполнения кода вычислений
# Пример:
#
# @LoggerDecorator
# def complex_algorithm(arg1, arg2):
#     # Здесь выполняется “сложный” алгоритм
#     result = 0
#     for i in range(arg1):
#         for j in range(arg2):
#             with open('test.txt', 'w', encoding='utf8') as file:
#                 file.write(str(i + j))
#                 result += i + j
#     # Можете попробовать вынести создание файла из циклов и проверить,
#          # сколько времени алгоритм будет работать в этом случае
#     return result
#
# # Пример вызова функции с применением декоратора
# result = complex_algorithm(10, 50)
# Вывод в консоли:
#
# Вызов функции complex_algorithm
# Аргументы: (10, 50), {}
# Результат: 14500
# Время выполнения: 0.20143938064575195 секунд
# Советы
# Вспомните пример работы с классом-декоратором из видео «Декоратор как класс».
# Чтобы получить имя функции, используйте атрибут __name__: func.__name__


import time
from typing import Callable
import functools


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)    # метод, которому передаем оборачиваемую функцию для избежания проблем декораторов
        self.func = func

    def __call__(self, *args, **kwargs):    # делает из класса декоратор
        # x() - это тоже самое, что x.__call__
        # позвояет любому экземпляру класса быть вызванным так, будто он - функция
        # смысл метода __call__ такоой же, как у функции wrapper
        start_time = time.time()     # Записываем время до вычислений
        print(f'Аргументы: {args}, {kwargs}')
        result_func = self.func(*args, *kwargs)
        time.sleep(1)
        end_time = time.time()     # Затем записываем время после вычислений
        execution_time = end_time - start_time     # Их разница будет временем выполнения кода вычислений
        print(f'Результат вычислений: {result_func}')
        print(f'Время выполнения кода вычислений {execution_time}')

        return result_func


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется “сложный” алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    # Можете попробовать вынести создание файла из циклов и проверить,
         # сколько времени алгоритм будет работать в этом случае
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)




# Решение SKILLBOX (можно реализовать лучше, см. модуль 17):
#
# import functools
#
#
# def singleton(cls):
#     """ Декоратор класса. Превращает класс в синглтон (может иметь только один инстанс). """
#
#     @functools.wraps(cls)
#     def wrapper_singleton(*args, **kwargs):
#         # ВТОРЫМ ЭТАПОМ реализуем логику - если в первый раз создаем объект класса, то помещаем его в кеш:
#         if not wrapper_singleton.instance:
#             wrapper_singleton.instance = cls(*args, *kwargs)
#         return wrapper_singleton.instance
#         # Т.о. даже если создадим объект снова, вернем все равно то, что записалось в кеш.
#
#     # ПЕРВЫМ ЭТАПОМ нужно сделать, чтобы у класса Example было не более одного экземпляра.
#         # Как это обозначить? Для этого создадим в декораторе переменную,
#             # которая будет служить кешем - хранилищем для уже рассчитанных данных: instance = None
#     # Если в классе уже есть объект класса, то отдаем его, если нет, то вычисляем его, поэтому надо сделать так:
#     wrapper_singleton.instance = None  # кеш
#     return wrapper_singleton
#
#
# ---- ИСХОДНЫЕ ДАННЫЕ --------------
# @singleton
# class Example:
#     pass
#
#
# my_obj = Exemple()
# my_another_obj = Exemple()
#
# print(id(my_obj))
# print(id(my_another_obj))
#
# print(my_obj is my_another_obj)
