# Часть 1. Модуль 5. Задача 6. Новоселье
#
# Есть два варианта:
# Выбрать квартиру попросторнее (не менее 100 м2), но стоимостью не более 10 млн.
# Немного расширить круг поиска, то есть выбрать квартиру поменьше (от 80 м2),
# но и стоимостью не более 7 млн.
# Напишите программу, которая получает на вход стоимость квартиры и
# её площадь и выводит сообщение, подходит ли она.
#
# Что оценивается
# результат вычислений корректен;
# input содержит корректное приглашение для ввода;
# в выводе программы указано, подходит ли данный параметр;
# переменные имеют значащие имена, а не только a, b, c, d (видео 2.3);
# правильное употребление пробелов после запятых и при бинарных операциях.

price = int(input('Введите стоимость квартиры, млн. руб: '))
square = int(input('Введите площадь квартиры, м^2: '))
if (square >= 100 and price <= 10) or (square >= 80 and price <= 7):
    print('Квартира подходит.')
else:
    print('Квартира не подходит.')
