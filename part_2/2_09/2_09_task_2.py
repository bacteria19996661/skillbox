# Часть 2. Модуль 9. Практическая работа. Задача 2. Дзен Пайтона
#
# В файле zen.txt хранится так называемый Дзен Пайтона — текст философии
# программирования на языке Python. Выглядит он так:
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
#
# Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.
# Кстати, попробуйте открыть консоль Python и ввести команду import this.
#
# Результат работы программы:
# Namespaces are one honking great idea -- let's do more of those!
# If the implementation is easy to explain, it may be a good idea.
# If the implementation is hard to explain, it's a bad idea.
# Although never is often better than *right* now.
# …
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
# Входной файл назван так, как указано в задании.

import os

path = os.path.join('zen.txt')
abs_path = os.path.abspath(path)
print(abs_path)

zen_file = open(abs_path, 'r')
temp_list = [line for line in zen_file]
zen_file.close()

print(temp_list)
print(temp_list[::-1])

reversed_zen_file = open('reversed_zen.txt', 'w')
for i_temp in temp_list[::-1]:
    reversed_zen_file.write(i_temp)
reversed_zen_file.close()