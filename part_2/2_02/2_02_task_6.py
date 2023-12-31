# Часть 2. Модуль 2. Практическая работа. Задание 6. Бегущие цифры
#
# Дан список из N элементов и целое число K. Напишите программу, которая
# циклически сдвигает элементы списка вправо на K позиций.
# Используйте минимально возможное количество операций присваивания.
#
# Пример 1:
# Сдвиг: 1
# Изначальный список: [1, 2, 3, 4, 5]
# Сдвинутый список: [5, 1, 2, 3, 4]
#
# Пример 2:
# Сдвиг: 3
# Изначальный список: [1, 4, –3, 0, 10]
# Сдвинутый список: [–3, 0, 10, 1, 4]
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значащие имена, не только a, b, c, d. Подробнее об этом — в видео 2.3.

def var_1():
    i = 0
    id = i + step

    for elem in start_list:
        if id < len(start_list):
            end_list.insert(id, elem)
            id += 1
        elif id == len(start_list):
            id = 0
            end_list.insert(id, elem)
            id += 1
        else:
            print('Ошибка ввода: шаг превышает длину списка.')
            break
        i += 1

def var_2():
    srez_l = start_list[:step]
    srez_r = start_list[step:]
    end_list[1:step] = srez_r + srez_l

start_list = [1, 4, -3, 0, 10]
step = 2
end_list = []

var_2()

print(f"Стартовый список {start_list}\n"
      f"Сдвинутый список: {end_list}")
