# Часть 1. Модуль 7. Задача 5. Отрезок
#
# Напишите программу, которая считывает с клавиатуры два числа:
# a и b, — считает и выводит в консоль среднее арифметическое всех чисел
# из отрезка [a; b], кратных числу 3.
#
# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# в выводе присутствует описание результата;
# для решения используется конструкция for.

a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
multiple_three, count = 0, 0

for n in range(a, b + 1):
    if n % 3 == 0:
        multiple_three += n
        count += 1
print('Среднее арифметическое чисел, кратных трем на данном отрезке: ', multiple_three / count)
