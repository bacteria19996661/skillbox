#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 18. Практическая работа. Задача 1. Lorem ipsum
#
# Для макетов веб-страниц часто используется какой-нибудь текст-рыба —
# это условный, нередко бессмысленный текст-заполнитель. Пусть дан следующий сгенерированный текст:
#
# Напишите программу, которая обрабатывает этот текст и выводит список слов, состоящих ровно из четырёх букв.
#
# Результат:
# ['amet', 'elit', 'eget', 'quam', 'quis', 'quis', 'enim', 'pede']
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Решение опирается на использование регулярных выражений и их методов.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).

import re

text = ('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. '
        'Aenean commodo ligula eget dolor. Aenean massa. '
        'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. '
        'Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. '
        'Nulla consequat massa quis enim. '
        'Donec pede justo, fringilla vel, aliquet nec, vulputate.')

result = re.findall(r'\b\w{4}\b', text)
print(result)



