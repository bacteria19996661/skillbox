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

    def __str__(self):
        return 'Вода'

    def __add__(self, other):

        if isinstance(other, Air):
            return Storm

        elif isinstance(other, Fire):
            return Steam

        elif isinstance(other, Earth):
            return Mud

        else:
            return None


class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):

        if isinstance(other, Water):
            return Storm

        elif isinstance(other, Fire):
            return Lightning

        elif isinstance(other, Earth):
            return Dust

        else:
            return None


class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):

        if isinstance(other, Air):
            return Lightning

        elif isinstance(other, Earth):
            return Lava

        elif isinstance(other, Water):
            return Steam

        else:
            return None


class Earth:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust

        elif isinstance(other, Fire):
            return Lava

        elif isinstance(other, Water):
            return Mud

        else:
            return None


class Storm:
    def __str__(self):
        return 'Шторм'

    def __call__(self, x, y):
        return x + y


class Steam:
    def __str__(self):
        return 'Пар'

    def __call__(self, x, y):
        return x + y


class Mud:
    def __str__(self):
        return 'Грязь'

    def __call__(self, x, y):
        return x + y


class Lightning:
    def __str__(self):
        return 'Молния'

    def __call__(self, x, y):
        return x + y


class Dust:
    def __str__(self):
        return 'Пыль'

    def __call__(self, x, y):
        return x + y


class Lava:
    def __str__(self):
        return 'Лава'

    def __call__(self, x, y):
        return x + y


water = Water()
air = Air()
fire = Fire()
earth = Earth()

# print(water)

storm = Storm()
steam = Steam()
mud = Mud()
lightning = Lightning()
dust = Dust()
lava = Lava()

storm.__call__(water, air)
steam.__call__(water, fire)
mud.__call__(water, earth)
lightning.__call__(air, fire)
dust.__call__(air, earth)
lava.__call__(fire, earth)

print(storm, steam, mud, lightning, dust, lava)
