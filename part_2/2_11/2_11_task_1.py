# Часть 2. Модуль 11. Практическая работа. Задача 1. Драка
#
# Есть два юнита, каждый называется «Воин».
# Каждому устанавливается здоровье в 100 очков.
# Они бьют друг друга в случайном порядке.
# Тот, кто бьёт, здоровье не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
#
# Реализуйте такую программу.
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# Сообщения о процессе получения результата осмысленны и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.

import random


class Warrior:

    def __init__(self, number, health=100, damage=20):
        self.number = number
        self.health = health
        self.damage = damage
        self.attack = random.getrandbits(1)

    def taking_damage(self):
        if self.health > 0:
            self.health -= self.damage
        print(f'Воин {self.number} получил урон. Осталось {self.health} здоровья.\n')

    def is_death(self):
        if self.health == 0:
            return True
        return False

    def is_attack(self):
        if self.attack == 1:
            print(f'Воин {self.number} атаковал и нанес {self.damage} урона.')
            return True
        return False

    def unit_info(self):
        print(f'Воин {self.number}: {self.health} здоровья.')


def battle(unit_1, unit_2):
    while not (unit_1.is_death() or unit_2.is_death()):
        print('-'*40, '\nБой начался!')
        if unit_1.is_attack():
            unit_2.taking_damage()
        elif unit_2.is_attack():
            unit_1.taking_damage()
        else:
            print('В сражении никто не пострадал.\n')
        print('Бой окончен. Итоги сражения: ')
        unit_1.unit_info()
        unit_2.unit_info()
        print()

    if unit_1.is_death():
        print('Победил Воин 2!')
    else:
        print('Победи Воин 1!')


if __name__ == '__main__':
    warrior_1 = Warrior(1)
    warrior_2 = Warrior(2)

    battle(warrior_1, warrior_2)
