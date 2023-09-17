# Часть 2. Модуль 11. Практическая работа. Задача 5. Совместное проживание
#
# Нужно реализовать модель человека и модель дома.
#
# Человек может (должны быть такие методы):
# есть (+ сытость, ? еда);
# работать (? сытость, + деньги);
# играть (? сытость);
# ходить в магазин за едой (+ еда, ? деньги);
# прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).
#
# У человека есть (должны быть такие атрибуты):
# имя,
# степень сытости (изначально 50),
# дом.
#
# В доме есть:
# холодильник с едой (изначально 50 еды),
# тумбочка с деньгами (изначально 0 денег).
# Если сытость человека становится меньше нуля, человек умирает.
#
# Логика действий человека определяется следующим образом:
#
# Генерируется число кубика от 1 до 6.
# Если сытость < 20, то нужно поесть.
# Иначе, если еды в доме < 10, то сходить в магазин.
# Иначе, если денег в доме < 50, то работать.
# Иначе, если кубик равен 1, то работать.
# Иначе, если кубик равен 2, то поесть.
# Иначе играть.
# По такой логике эксперимента человеку надо прожить 365 дней.
#
# Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз.
#
# Советы и рекомендации
# В большинстве случаев классы нужны не для того, чтобы с ними работать напрямую,
# а чтобы с их помощью создавать объекты, которые будут содержать необходимую информацию
# и смогут вызывать нужные методы. Наш случай не исключение:
# вам не нужно работать напрямую с классами, работайте с объектами, которые создаются при помощи этих классов.
# Глобальные переменные создают зависимости.
# Чем больше класс обращается к переменным, созданным снаружи класса, тем больше в классе появляется неопределённости
# (для работы с классом вам придётся отслеживать значения всех этих переменных).
# Передавайте нужные данные в объект и записывайте их в атрибуты вместо обращения к глобальной переменной.
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# Код можно использовать для создания нескольких людей, живущих в отдельных домах.
# Сообщения о процессе получения результата осмысленны и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.

import random
import string


class Human:
    day = 0

    def __init__(self, name, satiety_degree=50):
        self.name = name
        self.satiety_degree = satiety_degree    # степень сытости (изначально 50)

    def eating(self):     # есть (+ сытость, ? еда)
        print(f"{self.name} ест.")
        if house.fridge >= number:
            self.satiety_degree += number
            house.fridge -= number
        else:
            self.satiety_degree += house.fridge
            house.fridge = 0

    def go_to_shop(self):    # ходить в магазин за едой (+ еда, ? деньги)
        print(f"{self.name} идет в магазин.")
        if house.wallet >= number:
            house.fridge += number
            house.wallet -= number
        else:
            house.fridge += house.wallet
            house.wallet = 0

    def working(self):    # работать (? сытость, + деньги)
        print(f"{self.name} работает.")
        if self.satiety_degree >= number:
            house.wallet += number
            self.satiety_degree -= number
        else:
            house.wallet += 1
            self.satiety_degree -= 2

    def gaming(self):    # играть (? сытость)
        print(f"{self.name} играет.")
        self.satiety_degree -= 1

    def is_death(self):    # Если сытость человека становится меньше нуля, человек умирает
        if self.satiety_degree < 0:
            print(f"{self.name} покинул этот мир...")
            return True

    def living_day(self):    # прожить один день (выбирает одно действие по приоритету и выполняет его)
        self.human_info()
        if self.satiety_degree < 20:
            self.eating()
        elif house.fridge < 10:    # Иначе, если еды в доме < 10, то сходить в магазин.
            self.go_to_shop()
        elif house.wallet < 50:
            self.working()
        elif number == 1:
            self.working()
        elif number == 2:
            self.eating()
        else:
            self.gaming()

    def human_info(self):
        print("{} имеет степень сытости = {}".format(self.name, self.satiety_degree))


class House:
    def __init__(self):
        self.residents = [
            Human((''.join([random.choice(string.ascii_lowercase)
                            for _ in range(random.randint(1, 10))])).title()) for _ in range(2)]
        self.fridge = 50    # холодильник с едой (изначально 50 еды)
        self.wallet = 0     # тумбочка с деньгами (изначально 0 денег)

    def house_info_name(self):
        print("Жильцы дома:")
        for el in [i_human.name for i_human in self.residents]:
            print("    ", el)
        self.house_info()

    def house_info(self):
        print(f"Еды в холодильнике: {self.fridge}, денег: {self.wallet}.\n")


def life_round():
    day = 0
    for i_human in house.residents:
        print("-" * 40)
        while day < 365:
            if i_human.is_death():
                break
            else:
                i_human.living_day()
                day += 1
                print(f"Так прошел {day}-й день...\nИтоги дня:")
                house.house_info()
        day = 0
        if not i_human.is_death():
            print(f"{i_human.name} прожил 1 год!\n")


if __name__ == '__main__':
    house = House()
    house.house_info_name()
    number = random.randint(1, 6)  # Генерируется число кубика от 1 до 6
    life_round()
