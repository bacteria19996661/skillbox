#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Часть 2. Модуль 15. Практическая работа. Задача 2. Математический модуль
#
# Реализовать модуль дя математических вычислений, связанных с фигурами (нахождение площадей или периметров).
# Чтобы не захламлять код огромным количеством функций, выделить для них отдельный класс,
# подключить как модуль и использовать по аналогии с модулем math.
#
# Класс MyMath дожен состоять, как минимум, из следующих методов (добавить и другие методы):
# вычисление длины окружности,
# вычисление площади окружности,
# вычисление объёма куба,
# вычисление площади поверхности сферы.

# Пример основного кода:
# res_1 = MyMath.circle_len(radius=5)
# res_2 = MyMath.circle_sq(radius=6)
# print(res_1)
# print(res_2)
# Результат:
# 31.41592653589793
# 113.09733552923255
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений приватных атрибутов используются сеттеры и геттеры
# с соответствующими декораторами.
# Для создания нового класса на основе уже существующего используется наследование.
# Для статических и классовых методов используется декоратор classmethod.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs).
# Если функция/метод ничего не возвращает, то используется None.


from mymath import MyMath
MyMath = MyMath()

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.sphere_sq(radius=7)
res_4 = MyMath.cube_vol(a=8)

print(f'Длина окружности = {res_1}')
print(f'Площадь круга = {res_2}')
print(f'Площадь поверхности сферы = {res_3}')
print(f'Объём куба = {res_4}')
