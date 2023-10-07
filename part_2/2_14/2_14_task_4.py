#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Часть 2. Модуль 14. Практическая работа. Задача 4. Счётчик
#
# Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.
#
# Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).
#
# Что оценивается
# Результат вычислений корректен.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs).
# Если функция/метод ничего не возвращает, то используется None.
# Во всех декораторах используется functools.wraps().

import random
from typing import Callable, Any
import functools


def counter(func: Callable) -> Callable:
    """ Декоратор, который считает количество вызовов декорируемой функции"""

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        wrapped_func.count += 1
        result = func(*args, **kwargs)
        print('{func} вызвана {count} раз(а).'.format(func=func, count=wrapped_func.count))
        return result, wrapped_func.count

    wrapped_func.count = 0

    return wrapped_func

@counter
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(1000)])

    return result


number = random.randint(3, 10)
my_cubes_sum, quantity = 0, 0

for _ in range(number):
    my_cubes_sum, quantity = cubes_sum(200)

print(f"\nРезуьтат выполнния функции: {my_cubes_sum}, кол-во вызовов: {quantity}")



# Решение 2. Реализация через класс
# class Counter:
#     def __init__(self):
#         self.counter = 0
#     def increment(self):
#         self.counter += 1
#         return self.counter
#
# count = Counter()
# for _ in range(4):
#     print(count.increment())



# Решение 3. Реализация через класс-декоратор
# class Decorator:
#     count = 0
#
#     def __init__(self, func):
#         self.__func = func
#
#     @property
#     def get_func(self):
#         return self.__func
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         return self.__func(*args, **kwargs)
#
#
# @Decorator
# def cubes_sum(number: int) -> int:
#     result = 0
#     for _ in range(number + 1):
#         result += sum([i_num**3 for i_num in range(1000)])
#
#     return result
#
#
# for _ in range(10):
#     cubes_sum(10**3)
# print({cubes_sum.count})
