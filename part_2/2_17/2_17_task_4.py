#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 17. Практическая работа. Задача 4. Уникальный шифр
#
# Представьте, что вы — детектив, который получил загадочное письмо с шифровкой.
# Нужно найти количество уникальных символов в письме, чтобы разгадать его и раскрыть тайну.
#
# Задача
# Напишите функцию, которая принимает строку и возвращает количество уникальных символов в строке.
# Используйте для выполнения задачи lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного регистра должны считаться одинаковыми.
#
# Советы
# Работать с регистрами помогут методы строк lower/upper.
# Уникальными считаются буквы, которые повторяются только один раз
# (например строка «аа» будет содержать 0 уникальных букв).
#
# Пример:
# message = "Today is a beautiful day! The sun is shining and the birds are singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)
# Вывод: количество уникальных символов в строке — 5.

from collections import Counter

# def count_unique_characters(some_string):    # Еще альтернативный способ
#     return sum(1 for var in Counter(some_string.lower()).values() if var == 1)

if __name__ == '__main__':
    count_unique_characters = lambda x: sum(1 for var in Counter(x.lower()).values() if var == 1)
    message = "Today is a beautiful day! The sun is shining and the birds are singing."
    unique_count = count_unique_characters(message)
    if unique_count == 0:
        print("В строке нет уникальных символов.")
    else:
        print("Количество уникальных символов в строке:", unique_count)


# Моё альтернативное решение:
# def count_unique_characters(some_string: str):
#     """Функция для подсчета уникальных символов в строке.
#     Использует Counter для подсчета количества каждого символа в строке,
#     а затем с помощью генератора списка считает количество символов, встречающихся только один раз"""
#     cnt = Counter(some_string.lower())
#     return sum(1 for var in cnt.values() if var == 1)
