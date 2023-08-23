# Часть 2. Модуль 8. Практическая работа. Задача 4. Продвинутая функция sum
#
# Напишите свою функцию sum, которая должна быть более гибкой, чем стандартная.
# Она должна уметь складывать числа: из списка списков, из набора параметров.
# Основной код оставьте пустым или закомментированным (используйте его только для тестирования).
#
# Примеры вызовов функции
# sum([[1, 2, [3]], [1], 3])
# Ответ в консоли: 10
# sum(1, 2, 3, 4, 5)
# Ответ в консоли: 15
#
# Что оценивается
# Результат вычислений корректен.
# Весь функционал описан в отдельной функции.
# Переменные и функции имеют значимые имена, не только a, b, c, d.


def sum_args(*args):
    summ = 0
    for i_num in args:
        summ += i_num
    return summ
def sum_in(structure):
    if isinstance(structure, tuple):
        structure = list(structure)
    if structure == [] or ():
        return 0
    if isinstance(structure[0], (list, tuple)):
        return sum_in(structure[0]) + sum_in(structure[1:])
    return structure[0] + sum_in(structure[1:])

def full_sum(structure, *args):
    return sum_in(structure) + sum_args(*args)



if __name__ == '__main__':
    test_sample = [
        [[1, 2, [3]], [1], 3],                         # Ответ в консоли: 10
        (1, 2, 3, 4, 5),                               # Ответ в консоли: 15
        [[1, 2, [3], (11, (12, 15, 16), 13)], [1], 3], # Ответ в консоли: 77
        (1, (10, 20, [400, 500, 600], 30), 3, 4, 5)   # Ответ в консоли: 1573
    ]

    for sample in test_sample:
        print(f"Сумма элементов конструкции {sample} = {sum_in(sample)}")
    print(f"\nСумма аргументов = {sum_args(1, 2, 3, 4, 5)}\n")     # Ответ в консоли: 15

    for sample in test_sample:
        print(f"Общая сумма элементов конструкции с аргументами f({sample}, 1, 2, 3, 4, 5) = {full_sum(sample, 1, 2, 3, 4, 5)}")