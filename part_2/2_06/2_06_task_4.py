# Часть 2. Модуль 6. Практическая работа. Задание 4. Гистограмма частоты — 2
#
# Написать функцию, которая будет инвертировать полученный словарь.
# В качестве ключа будет частота, а в качестве значения — список символов с этой частотой.
#
# По итогу нужно реализовать следующие подзадачи:
# получить текст и создать из него оригинальный словарь частот;
# создать новый словарь и заполнить его данными из оригинального словаря частот,
# используя количество повторов в качестве ключей, а буквы — в качестве значений,
# добавляя их в список для хранения.
#
# Пример
# Введите текст: здесь что-то написано
# Оригинальный словарь частот:
# : 2
# - : 1
# З : 1
# а : 2
# д : 1
# е : 1
# и : 1
# н : 2
# о : 3
# п : 1
# с : 2
# т : 2
# ч : 1
# ь : 1
#
# Инвертированный словарь частот:
# 1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
# 2 : ['с', ' ', 'т', 'н', 'а']
# 3 : ['о']
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значимые имена, не только a, b, c, d.


def dict_frequencies(some_text):
    dict_rate = dict()
    some_text = sorted(some_text)
    for sym in some_text:
        dict_rate[sym] = some_text.count(sym)

    print("\nОригинальный словарь частот:")
    for i_rate in dict_rate:
        print(f"{i_rate} : {dict_rate[i_rate]}")

    return dict_rate


def inverted_dict(some_dict):

    inv_dict = dict()
    for el in set(some_dict.values()):
        inv_dict[el] = [key for key, val in some_dict.items() if val == el]

    print("\nИнвертированный словарь частот:")
    for i_inv in inv_dict:
        print(f"{i_inv}: {inv_dict[i_inv]}")

    return inv_dict



if __name__ == '__main__':
    text = input("Введите текст: ")
    inverted_dict(dict_frequencies(text))
