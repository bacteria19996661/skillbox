# Часть 2. Модуль 11. Практическая работа. Задача 3. Отцы, матери и дети
# Что нужно сделать
# Реализуйте два класса: «Родитель» и «Ребёнок».
#
# У родителя есть:
# имя,
# возраст,
# список детей.
#
# И он может:
# сообщить информацию о себе,
# успокоить ребёнка,
# покормить ребёнка.
#
# У ребёнка есть:
# имя,
# возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# состояние спокойствия,
# состояние голода.
#
# Реализация состояний — на ваше усмотрение.
# Это может быть и простой «флаг», и словарь состояний, и что-то поинтереснее.
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.

import random
import string


def gen_name():
    return (''.join([random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 10))])).title()


class Kid:
    def __init__(self, number):
        self.number = number
        self.kid_name = gen_name()
        self.kid_age = random.randint(0, 10)
        self.state_hunger = random.randint(0, 1)
        self.state_calm = random.randint(0, 1)

    def state_hunger(self):    # состояние голода
        if self.state_hunger == 1 or True:
            return True
        return False

    def state_calm(self):    # состояние спокойствия
        if self.state_hunger:
            return False
        else:
            self.state_calm = random.randint(0, 1)
            if self.state_calm == 1 or True:
                return True
            return False

    def kid_info(self):
        print("Номер: {}\nИмя: {}\nВозраст: {}\nРебенок спокоен: {}\nРебенок голоден: {}\n".format(
            self.number, self.kid_name, self.kid_age, self.state_calm, self.state_hunger
        ))


class Parent:
    def __init__(self, count_kids=1):
        self.name = gen_name()
        self.age = random.randint(26, 50)
        self.kids_list = [Kid(number) for number in range(1, count_kids+1)]

    def calm_down(self):    # успокоить ребёнка
        kid.state_calm = True

    def feed_baby(self):    # покормить ребёнка
        kid.state_hunger = False

    def parent_info(self):    # сообщить информацию о себе
        print("Имя: {}\nВозраст: {}\nСписок детей:\n------------------------\n".format(self.name, self.age))


numbers = random.randint(1, 20)
parent = Parent(numbers)
parent.parent_info()

kids = [Kid(number) for number in range(1, numbers + 1)]
for i, kid in enumerate(kids):
    kid.kid_info()

print('-'*80)

for i, kid in enumerate(kids):
    if kid.state_hunger:
        parent.feed_baby()
    if not kid.state_calm:
        parent.calm_down()
    kid.kid_info()
