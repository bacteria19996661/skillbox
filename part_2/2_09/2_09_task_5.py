# Часть 2. Модуль 9. Практическая работа. Задача 5. Частотный анализ
#
# Есть файл text.txt, который содержит текст.
# Напишите программу, которая выполняет частотный анализ, определяя долю каждой буквы английского алфавита
# в общем количестве английских букв в тексте, и выводит результат в файл analysis.txt.
# Символы, не являющиеся буквами английского алфавита, учитывать не нужно.
#
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте,
# с тремя знаками в дробной части. Буквы должны быть отсортированы по убыванию их доли.
# Буквы с равной долей должны следовать в алфавитном порядке.
#
# Пример:
# Содержимое файла text.txt:
# Mama myla ramu.
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
# Входные и выходные файлы названы так, как указано в задании.

def dictionary_creation(some_str):                 # формируем словарь из букв латиницы и их кол-ва
    sym_dict = dict()
    count = 0
    for sym in some_str:                           # проходим по символам в строке
        if ord("a") <= ord(sym) <= ord('z'):       # если символ - это буква латинского алфавита
            count += 1                             # считаем все буквы латинского алфавита в тексте
            sym_dict[sym] = some_str.count(sym)    # то считаем кол-во таких символов в строке и создаем запись в словаре
    return sym_dict, count

def dictionary_reverse_key_val(some_dict: dict):     # создаем обратный словарь из ключей и списков значений, где
    sym_sort_dict = dict()                               # ключ - это значение исходнного словаря, а значения - это ключи исходного словаря
    for key, val in some_dict.items():               # идем по ключам и значениям исходного словаря
        if val not in sym_sort_dict:                 # если элемента еще нет в создаваемом словаре
            sym_sort_dict[val] = list(key)           # создаем ключ нового словаря по значению исходного словаря,
        else:                                            # а значением будет список ключей исходного словаря
            sym_sort_dict[val].append(key)           # иначе добавляем в список ключей еще один ключ
    return sym_sort_dict

def dictionary_sorting(some_dict: dict, counter, file_name='analysis.txt'):    # сортируем словарь и записываем результат в файл
    with open(file_name, 'w') as analysis:
        for key in sorted(some_dict.keys(), reverse=True):            # сортируем ключи в обратном порядке и идем по ним
            for val in sorted(some_dict[key]):                        # для значений в отсортированном списке значений конкретного ключа
                print(f'{val} {key/counter:.3f}', file=analysis)


if __name__ == '__main__':

    with open('text.txt', 'r') as text:
        text_str = text.read().lower()

    sym_dict, count_alpha = dictionary_creation(text_str)
    reverse_dict = dictionary_reverse_key_val(sym_dict)
    sort_dict = dictionary_sorting(reverse_dict, count_alpha)
