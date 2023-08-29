# Часть 1. Модуль 10. Задание 8. Яма (генератор ландшафта)
#
# Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:
#
# Что оценивается
# Задание считается успешно выполненным, если:
# формат вывода соответствует примеру;
# input содержит корректное приглашение для ввода.

# Моё решение:
def task_10_8_1(levels: int) -> None:

    row, new_row, rewerse_new_row = '', '', ''

    for level in range(levels, 0, -1):
        row += str(level)

    for level in range(levels):
        width = levels - level - 1
        new_row = row[0:level + 1] + '.' * width
        rewerse_new_row = new_row[::-1]
        print(new_row + rewerse_new_row)


# Верное решение:
def task_10_8_2():

    depth = int(input('Введите глубину ямы: '))

    for line in range(depth):
        for left_number in range(depth, depth - line - 1, -1):
            print(left_number, end='')
        point_count = 2 * (depth - line - 1)
        print('.' * point_count, end='')
        for rignt_number in range(depth - line, depth + 1):
            print(rignt_number, end='')
        print()

#task_10_8_1()
task_10_8_2()
