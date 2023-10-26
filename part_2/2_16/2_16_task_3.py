#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Часть 2. Модуль 16. Практическая работа. # Задача 3. Логирование в формате
#
# Реализуйте декоратор, который будет логировать все методы декорируемого класса
# (кроме магических методов) и в который можно передавать формат вывода даты и времени логирования.
#
# Пример кода, передаётся формат «месяц день год — часы:минуты:секунды»:
#
# @log_methods("b d Y — H:M:S")
# class A:
#     def test_sum_1(self) -> int:
#         print('test sum 1')
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
# @log_methods("b d Y - H:M:S")
# class B(A):
#     def test_sum_1(self):
#         super().test_sum_1()
#         print("Наследник test sum 1")
#
#
#     def test_sum_2(self):
#         print("test sum 2")
#         number = 200
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#
#         return result
#
# my_obj = B()
# my_obj.test_sum_1()
# my_obj.test_sum_2()
# Результат:
# Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Тут метод test_sum_1.
# Завершение 'A.test_sum_1', время работы = 0,187 s.
# Тут метод test_sum_1 у наследника.
# Завершение 'B.test_sum_1', время работы = 0,187 s.
# Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 — 21:50:37.
# Тут метод test_sum_2 у наследника.
# Завершение 'B.test_sum_2', время работы = 0,370 s.
#
# Совет: внимательно пересмотрите видео 29.4, если сталкиваетесь с трудностями в этой задаче.
#
# Что оценивается в задаче
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры
# с соответствующими декораторами.
# Для создания нового класса на основе уже существующего используется наследование.
# Для статических и классовых методов используется декоратор classmethod.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов, кроме args и kwargs.
# Если функция/метод ничего не возвращает, то используется None.


from datetime import datetime
from typing import Callable, Optional, Any
import functools
import time


def time_format(_func: Optional[Callable] = None, *, date_format: str = "%b %d %Y — %H:%M:%S") -> Callable:
    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            now = datetime.now()  # Получение текущей даты и времени
            # Форматирование даты и времени с использованием заданного шаблона
            formatted_date_time = now.strftime(date_format)
            print(f'Запускается {func.__name__}. Дата и время запуска: {formatted_date_time}')
            return func(*args, **kwargs)

        return wrapped_func

    if _func is None:
        return decorator
    else:
        return decorator(_func)


def timer(func: Callable) -> Callable:
    """ Декоратор. Выводит время работы функции """

    @functools.wraps(func)
    # декоратор wraps, которому передаем оборачиваемую функцию для избежания проблем декораторов
    def wrapped_func(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = round(end - start, 4)
        print(f'Завершение {func.__name__}, время работы = {run_time} s.')

        return result

    return wrapped_func


def log_methods(decorator: Callable) -> Callable:
    """ Декоратор класса, который логирует все методы класса, кроме магических методов,
    и в который можно передавать формат вывода даты и времени логирования.
    Принимает декоратор и применяет его ко всем методам класса. """
    @functools.wraps(decorator)
    def decorate(cls):
        # Далее нужно вытащить все методы класса. Используем специальную встроенную функцию dir
        # print(dir(cls)) - список абсолютно всех методов, наши будут в конце
        for method_name in dir(cls):     # тут идем только по названиям методов, но не по ним самим,
                        # но испоьзуя названия можем взять методы из класса в качестве объектов,
                        # поэтому для получения самого метода как объекта испоьзуем функцию getattr
            if method_name.startswith('__') is False:
                cur_method = getattr(cls, method_name)    # (класс, имя метода)
                decoreted_method = decorator(cur_method)    # декорируем нужные методы c пом. нужного декоратора
                # Теперь нужно заменить старый метод на новый с помощью setattr
                setattr(cls, method_name, decoreted_method)    # (класс, старый метод, новый метод)
        # Вернем сам класс
        return cls

    return decorate


@log_methods(time_format())
@log_methods(timer)
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods(time_format())
@log_methods(timer)
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test sum 1 у наследника.")

    def test_sum_2(self):
        print("Тут метод test sum 2 у наследника.")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()


# Решение 2:
# import time
# from datetime import datetime
#
# def log_methods(date_format: str):
#     def decorator(cls):
#         class DecoratedClass(cls):
#             def __getattribute__(self, attr_name):
#                 attr = super().__getattribute__(attr_name)
#                 if callable(attr) and not attr_name.startswith("__"):
#                     def wrapped_method(*args, **kwargs):
#                         start_time = time.time()
#                         now = datetime.now()
#                         formatted_date_time = now.strftime(date_format)
#                         print(f"Запускается '{attr_name}'. Дата и время запуска: {formatted_date_time}.")
#
#                         result = attr(*args, **kwargs)
#
#                         end_time = time.time()
#                         execution_time = end_time - start_time
#                         print(f"Завершение '{attr_name}', время работы = {execution_time:.3f} s.")
#
#                         return result
#
#                     return wrapped_method
#                 return attr
#
#         return DecoratedClass
#
#     return decorator
#
# @log_methods("%b %d %Y — %H:%M:%S")
# class A:
#     def test_sum_1(self) -> int:
#         print('Тут метод test_sum_1')
#         number = 100
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#         return result
#
# @log_methods("%b %d %Y — %H:%M:%S")
# class B(A):
#     def test_sum_1(self):
#         super().test_sum_1()
#         print("Тут метод test_sum_1 у наследника")
#
#     def test_sum_2(self):
#         print("Тут метод test_sum_2")
#         number = 200
#         result = 0
#         for _ in range(number + 1):
#             result += sum([i_num ** 2 for i_num in range(10000)])
#         return result
#
# my_obj = B()
# my_obj.test_sum_1()
# my_obj.test_sum_2()
