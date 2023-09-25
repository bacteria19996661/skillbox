#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 12. Практическая работа. Задача 3. Свой словарь
#
# Реализуйте класс MyDict, который будет вести себя точно так же, как и обычный словарь
# (попробуйте унаследовать его от оригинального dict), за исключением того,
# что метод get по умолчанию будет возвращать не None, а число 0.
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# Сообщения о процессе получения результата осмысленны и понятны пользователю.
# Переменные, функции и собственные методы классов имеют значащие имена, а не a, b, c, d.
# Классы и методы/функции имеют прописанную документацию.

import random
import string
# from collections import OrderedDict


def create_my_dict():
    """
    Генерация словаря с ключами из натуральных чисел.
    :return:
    """
    some_dict = {}
    for _ in range(random.randint(1, 20)):
        random_string = lambda: ''.join([random.choice(string.ascii_lowercase)
                                         for _ in range(random.randint(4, 12))])
        random_number = random.randint(1, 100)
        some_dict[random_number] = ' '.join((random_string().title(), random_string().title()))
    return some_dict

class MyDict(dict):
    """
    Класс мой словарь. Родитель dict

    Attributes:
        some_dict (dict): словарь генерируется функцией create_my_dict()
    """
    def __init__(self):
        """
        Инициализация касса. Перенимает данные от базового dict.
        """
        super().__init__()
        self.some_dict = create_my_dict()

    def __str__(self):
        """
        Построчный вывод словаря.
        :return: (str)
        """
        return '\n'.join(["{}: {}".format(key, value) for key, value in self.some_dict.items()])

    def sorted_dict(self):
        # sort_dict = OrderedDict()
        """
        Сортировка ключей словаря с выводом отсортированных по ключам пар.
        :return: (str)
        """
        for key in sorted(self.some_dict.keys()):
            print("{}: {}".format(key, self.some_dict[key]))
            # sort_dict[key] = self.some_dict[key]
       # return sort_dict

    def user_key(self):
        """
        Процедура проверки существования ключа.
        Если такого ключа нет, добавяем его в словарь и присваиваем значение 0
        В конце выводится отсортированный по ключам словарь.

        :key (int): пользоватеьский ввод
        """
        key = int(input('\nВведите ключ (число): '))
        self.some_dict.get(key, 0)
        if not self.some_dict.get(key):
            self.some_dict[key] = '0'
            print(f"Ключ {key} добавлен в словарь с нулевым значением.")
        else:
            print(f"Найден ключ {key}: Значение: {self.some_dict.get(key, 'Такого ключа в словаре нет.')}")
        self.sorted_dict()


if __name__ == '__main__':
    my_dict = MyDict()
    print(my_dict)
    try:
        my_dict.user_key()
    except (TypeError, ValueError, Exception) as err:
        print(f"Ошибка ввода ({err}, {type(err)}): введите число.")
