# Часть 1. Модуль 10. Задание 7. Пирамидка-2
#
# Напишите программу, которая получает на вход количество уровней пирамиды
# и выводит их на экран, заполняя нечётными числами:
#
# Что оценивается
# Задание считается успешно выполненным, если:
# формат вывода соответствует примеру;
# input содержит корректное приглашение для ввода.

# Решение 1:
def task_10_7_1(rows_pir: int) -> None:
    new_num = 1

    for line in range(rows_pir):
        for spase in range(rows_pir - line - 1, 0, -1):
            print(end = '   ')
        for number in range(line + 1):
            print(new_num, end = '    ')
            new_num += 2
        print()


# Решение 2 альтернативное:
def task_10_7_2(levels: int) -> None:
    current_number = 1

    for level in range(levels):
        spaces = " " * (levels - level - 1)
        row = ""
        for _ in range(level + 1):
            if current_number < 10:
                row += f" {current_number} "
            else:
                row += f"{current_number} "
            current_number += 2

        print(' ', spaces, row)

task_10_7_1(8)
# task_10_7_2(8)
