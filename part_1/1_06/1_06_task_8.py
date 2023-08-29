# Часть 1. Модуль 6. Задача 8. Игра «Компьютер угадывает число»
#
# Напишите программу, которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
# Cделайте так, чтобы можно было гарантированно угадать число за семь попыток.
#
# Подсказка
# При желании найдите описание алгоритма бинарного поиска и попробуйте применить в этой задаче. Разбор подобного решения будет в следующем модуле.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректное приглашение для ввода.
# Правильное употребление пробелов после запятых и при бинарных операциях.

# Решение 1:
def task_6_8_1():
    list_excess = []
    a, b, count = 1, 100, 0

    while True:
        count += 1
        N = (a + b) // 2
        list_excess.append(N)
        print()
        print('N =', N)
        answer = int(input('Твоё число равно(1), больше(2) или меньше(3) N?  '))
        if (answer == 2) and N == 99:
            N += 1
        if answer == 1:
            print()
            print('Я угадал! Это', N)
            print('Использовано попыток:', count)
            print(list_excess)
            break
        elif answer == 2:
            a = N + 1
        elif answer == 3:
            b = N - 1

# Решение 2:
def task_6_8_2():
    count = 0
    sec = int(input('Загадайте число: '))
    mn, mx = 1, 100
    tr, key = 0, 0
    
    while True:
        count += 1
        tr = (mx + mn) // 2
        print('Твое число: 1 - равно, 2 - больше или 3 - меньше, чем число', tr)
        key = int(input('Введите ответ: '))
        if key == 1:
            print('Угадал за', count, 'попыток')
            break
        elif key == 2:
            mn = tr
        elif key == 3:
            mx = tr

task_6_8_1()
