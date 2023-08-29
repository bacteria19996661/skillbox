# Часть 1. Модуль 5. Задача 1. Калькулятор опыта
#
# Напишите программу, которая определяет уровень персонажа в компьютерной игре.
# Пользователь вводит число «очков опыта», а программа вычисляет уровень.
# Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта».
# Начальный уровень равен единице.
#
# Пример:
# Введите количество опыта: 6000
# Ваш уровень: 4
# Пример 2:
# Введите количество опыта: 2000
# Ваш уровень: 2
#
# Советы и рекомендации
# По возможности уделите внимание сокращению кода.
# Постарайтесь не проверять условия, которые уже проверены:
# если вы проверили условие condition, то не следует проверять not condition.
#
# Что оценивается
# результат вывода корректен, особое внимание уделено границам диапазонов;
# input содержит корректное приглашение для ввода;
# переменные имеют значащие имена, а не только a, b, c, d (видео 2.3);
# правильное употребление пробелов после запятых и при бинарных операциях;
# правильно оформлены блоки if-elif-else, отступы одинаковы во всех блоках одного уровня.


experience = int(input('Введите кол-вол очков опыта: '))
if (experience >= 1000) and (experience < 2500):
    level = 2
elif (experience >= 2500) and (experience < 5000):
    level = 3
elif (experience >= 5000):
    level = 4
else:
    level = 1
print('Уровень персонажа', level)
