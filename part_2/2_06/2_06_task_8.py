# Часть 2. Модуль 6. Практическая работа. Задание 8. Снова палиндром
#
# Пользователь вводит строку. Необходимо написать программу, которая определяет,
# существует ли у этой строки перестановка, при которой она станет палиндромом.
# Затем она должна выводить соответствующее сообщение.
#
# Пример 1
# Введите строку: aab
# Можно сделать палиндромом
#
# Пример 2
# Введите строку: aabc
# Нельзя сделать палиндромом
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельной функции.
# Переменные и функции имеют значимые имена, не только a, b, c, d.
#

def replase_to__palindrom(some_str):
    sym_dict = dict()

    for sym in some_str:
        sym_dict[sym] = some_str.count(sym)

    count = 0
    for val in sym_dict.values():
        if val % 2 == 1:
            count += 1

    if count > 1:
        return f"Строку {some_str} нельзя сделать палиндромом."
    else:
        return f"Строку {some_str} можно сделать палиндромом."


if __name__ == '__main__':
    test_cases = [
        'aab',
        'aabc',
        'somestr',
        'atbggba',
        ''
    ]
    for some_str in test_cases:
        print(replase_to__palindrom(some_str))