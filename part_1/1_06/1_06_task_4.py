# Часть 1. Модуль 6. Задача 4. Поставьте оценку!
#
# Напишите программу, которая находит количество положительных и
# количество отрицательных чисел в последовательности.
# Последовательность заканчивается на числе 0.
#
# Пример
# Введите число: −4
# Введите число: −90
# Введите число: 6
# Введите число: 0
# Кол-во положительных чисел: 1
# Кол-во отрицательных чисел: 2
#
# Что оценивается:
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Input содержит корректное приглашение для ввода.
# Ввод чисел осуществляется внутри цикла.
# При вводе 0 происходит выход из цикла и производится вывод подсчитанных положительных и отрицательных чисел.
# Переменные имеют значащие имена, не только a, b, c, d (видео 2.3).
# Правильное употребление пробелов после запятых и при бинарных операциях.

count1 = 0
count2 = 0

while True:
    num = int(input('Введите число от -100 до 100 (для выхода намите 0): '))
    if num == 0:
        break
    elif num > 0:
        count1 += 1
    else:
        count2 += 1

print('Кол-во положительных чисел: ', count1)
print('Кол-во отрицательных чисел: ', count2)
