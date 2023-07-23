# Часть 2. Модуль 1. Задача 2. Сумма и разность
#
# Напишите две функции. Первая принимает одно целое положительное число N и находит сумму всех цифр в числе.
# Вторая принимает число N и считает количество цифр в числе.
# В ответ выводится разность суммы чисел и количества.
#
# Пример:
# Введите число: 500
# Сумма чисел: 5
# Количество цифр в числе: 3
# Разность суммы и количества цифр: 2
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Программа имеет две отдельные функции, описанные в условии задачи.
# Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).



def is_negative(number: int) -> bool:
    return number < 0


def summ_number(number: int):
    if is_negative(number):
        raise ValueError(f"Ошибка ввода. Введите целое положительное число.")

    summ = 0
    while number > 0:
        summ += number % 10
        number = number // 10

    return summ


def quality_number(number: int):
    if is_negative(number):
        raise ValueError(f"Ошибка ввода. Введите целое положительное число.")

    count = 0
    while number > 0:
        number = number // 10
        count += 1

    return count



if __name__ == '__main__':
    try:
        number = int(input('Введите число: '))
    except ValueError:
        print(f"Ошибка ввода. Введите целое положительное число.")
        number = int(input('Введите число: '))

    try:
        result = abs(summ_number(number) - quality_number(number))
        print(f"Разность суммы цифр и колл-ва цифр в числе {number}: {result}")
    except ValueError as e:
        print(e)
