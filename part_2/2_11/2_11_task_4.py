# Часть 2. Модуль 11. Практическая работа. Задача 4. Магия
#
# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый.
# У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля».
# Из них получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».
# Таблица преобразований:
# Вода + Воздух = Шторм;
# Вода + Огонь = Пар;
# Вода + Земля = Грязь;
# Воздух + Огонь = Молния;
# Воздух + Земля = Пыль;
# Огонь + Земля = Лава.
# Напишите программу, которая реализует все эти элементы.
# Каждый элемент необходимо организовать как отдельный класс.
# Если результат не определён, то возвращается None.
# Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:
#
# class ExampleOne:
#     def __add__(self, other):
#         return ExampleTwo()
#
# class ExampleTwo:
#     answer = 'сложили два класса и вывели'
#
# first_example = ExampleOne()
# second_example = ExampleTwo()
# result = first_example + second_example
# print(result.answer)
#
# Дополнительно: придумайте свой элемент (или элементы) и реализуйте его взаимодействие с остальными.
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.

class Water:
    def __init__(self):
        self.water = Water

    def __add__(self, other):
        if other == air:
            return Storm()
        elif other == fire:
            return Steam()
        elif other == earth:
            return Mud()
        else:
            print('Нет такой комбинации.')

    def __radd__(self, other):
        return self + other


class Air:
    def __init__(self):
        self.air = Air

    def __add__(self, other):
        if other == fire:
            return Lightning()
        elif other == earth:
            return Dust()
        elif other == water:
            return Storm()
        else:
            print('Нет такой комбинации.')

    def __radd__(self, other):
        return self + other


class Fire:
    def __init__(self):
        self.fire = Fire

    def __add__(self, other):
        if other == air:
            return Lightning()
        elif other == earth:
            return Lava()
        elif other == water:
            return Steam()
        else:
            print('Нет такой комбинации.')

    def __radd__(self, other):
        return self + other


class Earth:
    def __init__(self):
        self.earth = Earth

    def __add__(self, other):
        if other == air:
            return Dust()
        elif other == fire:
            return Lava()
        elif other == water:
            return Mud()
        else:
            print('Нет такой комбинации.')

    def __radd__(self, other):
        return self + other


class Storm:
    answer = 'Вода + Воздух = Шторм'


class Steam:
    answer = 'Вода + Огонь = Пар'


class Mud:
    answer = 'Вода + Земля = Грязь'


class Lightning:
    answer = 'Воздух + Огонь = Молния'


class Dust:
    answer = 'Воздух + Земля = Пыль'


class Lava:
    answer = 'Огонь + Земля = Лава'


water = Water()
air = Air()
fire = Fire()
earth = Earth()

# Вода + Воздух = Шторм
result_1 = water + air
print(result_1.answer)

# Вода + Огонь = Пар
result_2 = water + fire
print(result_2.answer)

# Вода + Земля = Грязь
result_3 = water + earth
print(result_3.answer)

# Воздух + Огонь = Молния
result_4 = air + fire
print(result_4.answer)

# Воздух + Земля = Пыль
result_5 = air + earth
print(result_5.answer)

# Огонь + Земля = Лава
result_6 = fire + earth
print(result_6.answer)
