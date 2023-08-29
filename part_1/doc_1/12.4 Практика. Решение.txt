# Задача 1. Среднее арифметическое
#
# Программа получает от пользователя два числа — a и b.
# Реализуйте функцию, которая принимает на вход числа a и b, считает
# и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b].
# Обеспечьте контроль ввода: не забывайте, что а всегда должно быть меньше, чем b.
#
#
#
# Пример:
#
# Введите левую границу: 3
#
# Введите правую границу: 8
#
# Среднее: 5.5
#
#
#
# Усложнение: сделайте это без использования циклов.
#
#
#
import math


def mean_calc(x, y):
    sum_of_numbers, count_of_numbers = 0, 0
    for i in range(x, y + 1):
        sum_of_numbers += i
        count_of_numbers += 1

    print("Среднее:", round(sum_of_numbers / count_of_numbers, 2))

    # Без цикла

    print("Среднее:", round((x + y) / 2, 2))


a = int(input("Введите a: "))
b = int(input("Введите b: "))

if a > b:
    a, b = b, a

mean_calc(a, b)


# Задача 2. Почта 2
#
# На почте немного поменялись правила: теперь в почтовом извещении нужно указывать
# фамилию, имя, страну проживания, город, улицу, номер дома и номер квартиры.
#
# Реализуйте функцию, которая получает все эти данные и выводит на экран.
# В программе вызовите функцию три раза с разными значениями аргументов.
#
#
#
# Подсказка: семь аргументов.
#
#
#

def print_all_info(surname, name, country, city, street, house, flat):
    print("Фамилия:", surname)
    print("Имя:", name)
    print("Страна проживания:", country)
    print("Город:", city)
    print("Улица:", street)
    print("Номер дома:", house)
    print("Номер квартиры:", flat)


# Вариант с форматированием строк (форматирование будет изучено позже)
def print_all_info_hard(surname, name, country, city, street, house, flat):
    print(f"Фамилия: {surname}\n"
          f"Имя: {name}\n"
          f"Страна проживания: {country}\n"
          f"Город: {city}\n"
          f"Улица: {street}\n"
          f"Номер дома: {house}\n"
          f"Номер квартиры: {flat}")


user_surname = input("Введите фамилию: ")
user_name = input("Введите имя: ")
user_street = input("Введите улицу: ")
user_house = input("Введите номер дома: ")

for _ in range(3):
    user_surname = input("Введите фамилию: ")
    user_name = input("Введите имя: ")
    user_country = input("Введите страну проживания: ")
    user_city = input("Введите город: ")
    user_street = input("Введите улицу: ")
    user_house = input("Введите номер дома: ")
    user_flat = input("Введите номер квартиры: ")

    print_all_info(user_surname, user_name, user_country, user_city, user_street, user_house, user_flat)


# Задача 3. GPS-навигатор 2.0
#
# Нам поручили усовершенствовать GPS-навигатор, добавив в него новую фишку.
# Теперь пользователь может не только смотреть расстояние от себя до объекта, но и задавать в навигаторе две произвольные точки,
# после чего на экран ему выводится расстояние между ними. Для этого пользователь вводит четыре действительных числа x1, y1, x2, y2 —
# это как раз координаты этих двух точек.
#
#
#
# Напишите программу, где у пользователя спрашивается, чего он хочет — найти расстояние от себя до точки или
# найти расстояние между двумя произвольными точками, после чего запрашиваются необходимые координаты точек и выводится ответ на экран.

def my_distance(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print(distance)


def their_distance(x_1, x_2, y_1, y_2):
    distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    print(distance)


user_choice = int(input("Найти расстояние от себя до точки (1) или найти расстояние между двумя произвольными точками (2)? "))
if user_choice == 1:
    target_x = float(input("Введите координату X цели: "))
    target_y = float(input("Введите координату Y цели: "))
    my_distance(target_x, target_y)
elif user_choice == 2:
    target_x_1 = float(input("Введите координату X цели 1: "))
    target_y_1 = float(input("Введите координату Y цели 1: "))
    target_x_2 = float(input("Введите координату X цели 2: "))
    target_y_2 = float(input("Введите координату Y цели 2: "))
    their_distance(target_x_1, target_x_2, target_y_1, target_y_2)
else:
    print("Ввод неверный")
