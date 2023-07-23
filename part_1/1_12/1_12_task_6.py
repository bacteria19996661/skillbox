# Модуль 12. Задача 6. НОД
#
# Напишите функцию, вычисляющую наибольший общий делитель двух чисел.
# Разложим на простые множители 18 = 2 • 3 • 3
# Разложим на простые множители 35 = 5 • 7
# Выберем одинаковые простые множители в обоих числах. Одинаковые простые множители отсутствуют
# Находим произведение одинаковых простых множителей и записываем ответ НОД (18; 35) = 1
#
# Что оценивается
# Результат вывода соответствует условию.
# В input содержится корректное приглашение для ввода.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).



import math


def n_o_d(number_1: int, number_2: int) -> int:

    nod = 1

    if number_1 > number_2:
        smaller = number_2
    else:
        smaller = number_1

    for i in range(1, smaller + 1):
        try:
            if((number_1 % i == 0) and (number_2 % i == 0)):
                nod = i
        except ZeroDivisionError:
            return 0
    return nod



if __name__ == '__main__':
    test_cases = [
        (12, 34),
        (34, 12),
        (49, 7),
        (350, 800),
        (200, 224),
        (1, 0),
        ]

    for number_1, number_2 in test_cases:

            result = n_o_d(number_1, number_2)
            print(f"Проверка функцией: {math.gcd(number_1, number_2)}")
            print(f"Наибольший общий делитель чисел {number_1} и {number_2}: {result}\n")
