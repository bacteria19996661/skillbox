# Часть 1. Модуль 12. Задача 2. Функция в функции
#
# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода.
# Это вызов функции test(). В ней запрашивается на ввод целое число.
# Если оно положительное, то вызывается функция positive(),
# тело которой содержит команду вывода на экран слова «Положительное».
# Если число отрицательное, то вызывается функция negative(),
# её тело содержит выражение вывода на экран слова «Отрицательное».
#
# Что оценивается
# Результат вывода соответствует условию.
# В input содержится корректное приглашение для ввода.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


def test():
    number = int(input('Введите целое число: '))
    if number >= 0:
        positive()
    else:
        negative()


if __name__ == '__main__':
    test()
