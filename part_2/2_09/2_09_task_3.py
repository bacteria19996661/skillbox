# Часть 2. Модуль 9. Практическая работа. Задача 3. Файлы и папки
#
# Напишите программу, которая получает на вход путь до каталога
# (в том числе это может быть просто корень диска) и
# выводит общее количество файлов и подкаталогов в нём.
# Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).
#
# Важный момент: чтобы посчитать, сколько весит каталог,
# нужно найти сумму размеров всех вложенных в него файлов.
# Результат работы программы на примере python_basic\Module14:
#
# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кбайтах): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Input содержит корректные приглашения для ввода.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).

import os

top_dir = input('Введите путь: ') # top_dir = os.path.abspath(os.path.join(os.sep))

def dir_info(path):
    count_dirs, count_files, full_files_size = 0, 0, 0
    for dir_path, dir_list, file_list in os.walk(path):
        for i_file in file_list:
            file_path = os.path.join(dir_path, i_file)
            full_files_size = os.path.getsize(file_path)
            count_files += 1
        count_dirs += 1

    # result_list = [(len(dirs), len(files), sum(getsize(join(root, name)) for name in files))
    #                for root, dirs, files in os.walk(path)]
    return count_dirs, count_files, full_files_size


dirs, files, full_size = dir_info(top_dir)

print(f"Кол-во подкаталогов: {dirs}\n"
      f"Кол-во файлов: {files}\n"
      f"Размер каталога, кБ: {(full_size / 1024):.2f}")
