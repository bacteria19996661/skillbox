#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 17. Практическая работа. Задача 3. Палиндром: возвращение
#
# Есть множество встроенных и внешних библиотек для работы с данными в Python.
# С некоторыми из них вы уже работали. Например, с модулем collections,
# когда использовали специальный класс OrderedDict, с помощью которого делали упорядоченный словарь.
# В этой библиотеке есть и другие возможности, но их немного.
# Официальная документация: collections — Container datatypes.
#
# Используя модуль collections, реализуйте функцию can_be_poly,
# которая принимает на вход строку и проверяет, можно ли получить из неё палиндром.
#
# Пример кода:
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True
# False
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Решение опирается на использование лямбда-функций.
# Классы и методы/функции имеют прописанную документацию, хотя бы минимальную.
# Есть аннотация типов для методов/функций и их аргументов, кроме args и kwargs.
# Если функция/метод ничего не возвращает, то используется None.

from collections import Counter


def can_be_poly(some_string: str) -> bool:
    cnt = Counter(some_string)
    return sum(1 for var in cnt.values() if var % 2 != 0) < 2


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))


# Мой неоптимизированный код:
# def can_be_poly(some_string: str) -> bool:
#     cnt = Counter()
#     for sym in some_string:
#         cnt[sym] += 1
#     temp = 0
#     for key, var in cnt.items():
#         if var % 2 != 0:
#             temp += 1
#     if temp < 2:
#         return True
#     return False
