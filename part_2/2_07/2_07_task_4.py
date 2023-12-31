# Часть 2. Модуль 7. Практическая работа. Задача 4. По парам
#
# Напишите программу, которая инициализирует список из 10 случайных целых чисел,
# а затем делит эти числа на пары кортежей внутри списка. Выведите результат на экран.
# Дополнительно: решите задачу несколькими способами.
# Пример:
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.
# Для решения используются list comprehensions.

import random

numbers = [random.randint(0, 100) for _ in range(10)]
print(f"Оригинальный список: {numbers}")

list_tup = [tuple(numbers[i:i+2]) for i in range(0, 10, 2)]
print(f"Новый список 1: {list_tup}")

numbers2 = list(zip([el for i, el in enumerate(numbers) if i % 2 == 0], [el for i, el in enumerate(numbers) if i % 2 != 0]))
print(f"Новый список 2: {numbers2}")
