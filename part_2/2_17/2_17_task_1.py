#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 17. Практическая работа. Задача 1. Новые списки
#
# Даны три списка:
# floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# 1. Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
# 2. Из списка names берутся только имена минимум из пяти букв.
# 3. Из списка numbers берётся произведение всех чисел.
#
# Что оценивается в задаче
# Результат вычислений корректен.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Решение опирается на использование лямбда-функций.

from typing import List
from functools import reduce

if __name__ == "__main__":

    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

    new_floats = list(map(lambda x: round(x**3, 3), floats))
    print(new_floats)

    new_names = list(filter(lambda x: len(x) >= 5, names))
    print(new_names)

    def mult(acc, some_list):
        return acc * some_list

    new_numbers = reduce(mult, numbers)
    print(new_numbers)