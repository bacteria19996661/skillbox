# Часть 1. Модуль 4. Задача 8. Максимальное число (по желанию)
#
# Пользователь вводит три числа. Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Используйте дополнительные переменные, если нужно.
#
# Что оценивается
# результат вычислений корректен;
# input содержит корректное приглашение для ввода;
# правильное употребление пробелов после запятых и при бинарных операциях.

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if num1 > num2 and num1 > num3:
    print('Максимальное число: ', num1)
elif num2 > num1 and num2 > num3:
    print('Максимальное число: ',num2)
else:
    print('Максимальное число: ',num3)
