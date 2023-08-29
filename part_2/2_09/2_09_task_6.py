# Часть 2. Модуль 9. Практическая работа. Задача 6. «Война и мир»
#
# «Война и мир» лежит в архиве voina-i-mir.zip.
# Напишите программу, которая подсчитывает статистику по буквам (не только русского алфавита)
# в этом романе и выводит результат на экран (или в файл).
# Результат должен быть отсортирован по частоте встречаемости букв (по возрастанию или убыванию).
# Регистр символов имеет значение.
#
# Архив можно распаковать вручную, но, если хотите, можете изучить документацию по модулю zipfile
# (можно использовать и другой модуль) и попробовать написать код, который будет распаковывать архив за вас.
#
# Что оценивается
# Результат вычислений корректен.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
# Входной файл назван так, как указано в задании, выходной файл имеет значащее имя.

import os
import zipfile
import time

def zip_extract(zip_file_path):    # Процедура извлечения файлов из архива в текущую директорию
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        zip_file.extractall()

def dict_creation(some_text):                    # формируем словарь из букв всех типов и их кол-ва
    start1 = time.perf_counter()
    sym_dict = dict()
    for line in some_text:                       # проходим по строкам в тексте
        for sym in line:                         # проходим по символам в строке
            if sym.isalpha():                    # если символ - это буква алфавита
                if sym not in sym_dict:          # если такого символа еще нет в ключах словаря
                    sym_dict[sym] = 1            # то добавляем этот символ в словарь в качестве ключа
                sym_dict[sym] += 1               # и в значение вписываем подсчет таких символов во всем тексте
    print(f"Time dict_creation: {time.perf_counter() - start1}")
    return sym_dict

def merge_dicts(dicts_list):    # Слияние словарей разных файлов
    start2 = time.perf_counter()
    merge_dict = dict()
    for i, elem in enumerate(dicts_list):
        for key, val in elem.items():
            if key not in merge_dict:
                merge_dict[key] = val
            else:
                merge_dict[key] += val
    print(f"Time merge_dicts: {time.perf_counter() - start2}")
    return merge_dict

def reverse_key_val(some_dict: dict):     # Создаем обратный словарь из ключей и списков значений, где
    start3 = time.perf_counter()
    sym_sort_dict = dict()                               # ключ - это значение исходнного словаря, а значения - это ключи исходного словаря
    for key, val in some_dict.items():               # идем по ключам и значениям исходного словаря
        if val not in sym_sort_dict:                 # если элемента еще нет в создаваемом словаре
            sym_sort_dict[val] = list(key)           # создаем ключ нового словаря по значению исходного словаря,
        else:                                            # а значением будет список ключей исходного словаря
            sym_sort_dict[val].append(key)           # иначе добавляем в список ключей еще один ключ
    print(f"Time reverse_key_val: {time.perf_counter() - start3}")
    return sym_sort_dict

def dict_sorting(some_dict: dict, file_name='vim_analysis.txt'): # Процедура сортировки словаря и записи результата в файл
    start4 = time.perf_counter()
    with open(file_name, 'w', encoding='cp1251') as analysis:
        for key in sorted(some_dict.keys(), reverse=True):                # сортируем ключи в обратном порядке и идем по ним
            for val in sorted(some_dict[key]):                   # для значений в отсортированном списке значений конкретного ключа
                print(f'{val} {key:.3f}', file=analysis)
    print(f"Time dict_sorting: {time.perf_counter() - start4}")

if __name__ == '__main__':
    archive_name = 'voyna_i_mir'
    zip_extract(archive_name + '.zip')
    sym_dict = dict()
    path_list = [os.path.join(os.path.abspath(archive_name), path) for path in os.listdir(archive_name)]

    dictionary_list = []
    for i, i_path in enumerate(path_list):
        with open(i_path, 'r', encoding='cp1251') as text:
            temp_dict = dict_creation(text)
            dictionary_list.append(temp_dict)

    merge_dict = merge_dicts(dictionary_list)
    reverse_merge_dict = reverse_key_val(merge_dict)
    sort_merge_dict = dict_sorting(reverse_merge_dict)