#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 12. Практическая работа. Задача 2. Карма
#
# Один буддист-программист решил создать свой симулятор жизни, в котором нужно
# набрать 500 очков кармы (это константа), чтобы достичь просветления.
#
# Каждый день вызывается специальная функция one_day(), которая возвращает
# количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:
# KillError,
# DrunkError,
# CarCrashError,
# GluttonyError,
# DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
#
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого
# возможен только при накоплении кармы до уровня константы.
# Исключения обработайте и запишите в отдельный лог karma.log.
#
# По итогу у вас может быть примерно такая структура программы:
# открываем файл
# цикл по набору кармы
#    try
#       карма += one_day()
#    except(ы) с указанием классов исключений, которые нужно поймать
#       добавляем запись в файл
# закрываем файл
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
# Для создания нового класса на основе уже существующего используется наследование.
# Сообщения о процессе получения результата осмысленны и понятны пользователю.
# Переменные, функции и собственные методы классов имеют значащие имена, а не a, b, c, d.
# Классы и методы/функции имеют прописанную документацию.
# Названия используемых файлов соответствуют тем, которые указаны в задаче.

import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    carma = random.randint(1, 7)
    accident = random.randint(0, 100)
    if accident == 0:
        print(f"Сработало исключение ({accident})")
        match carma:
            case 1:
                raise KillError('Ошибка KillError')
            case 2:
                raise DrunkError('Ошибка DrunkError')
            case 3:
                raise CarCrashError('Ошибка CarCrashError')
            case 4:
                raise GluttonyError('Ошибка GluttonyError')
            case 5:
                raise DepressionError('Ошибка DepressionError')
            case _:
                raise Exception('Другая ошибка.')
    else:
        return carma


const = 500
sum_carma = 0
while sum_carma < const:
    sum_carma += one_day()
    print(f"Карма: {sum_carma}")
