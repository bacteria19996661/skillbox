# Часть 2. Модуль 2. Практическая работа. Задание 1. Страшный код
#
# Есть один основной (‘a’) и два побочных списка (‘b’ и ‘c’),
# в основном лежат элементы [1, 5, 3], а в побочных — [1, 5, 1, 5] и [1, 3, 1, 5, 3, 3] соответственно.
#
# Программа добавляет элементы побочного списка ‘b’ в основной, а затем считает количество цифр 5.
# Это число выводится на экран, и после этого цифры 5 удаляются из основного списка.
# Затем программа добавляет в основной список элементы списка ‘c’,
# считает количество цифр 3 и выводит это число на экран.
# В конце появляется и сам список.
#
# Код:
# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
# a.append(i)
# t = 0
# for i in a:
# if i == 5:
# t += 1
# print(t)
# d = []
# for i in a:
# if i != 5:
# d.append(i)
# for i in c:
# d.append(i)
# t = 0
# for i in d:
# if i == 3:
# t += 1
# print(t)
# print(d)
# Используя знания о методах списков, а также о стиле программирования,
# помогите другу переписать программу. Не используйте дополнительные списки.
#
# Результат работы программы:
# Количество цифр 5 при первом объединении: 3
# Количество цифр 3 при втором объединении: 4
# Итоговый список: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

list_a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

list_a.extend(b)
print(f"Количество цифр 5 при первом объединении: {list_a.count(5)}")
while 5 in list_a:
    list_a.remove(5)
print(f"Cписок: {list_a}")
list_a.extend(c)
print(f"Количество цифр 3 при втором объединении: {list_a.count(3)}")
print(f"Итоговый список: {list_a}")
