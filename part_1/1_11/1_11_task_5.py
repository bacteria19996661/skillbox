# Часть 1. Модуль 11. Задача 5. Вот это объемы!
#
# Есть формула для подсчета объема шара:
#
# где V — это объём, π — число пи, а R — радиус планеты.
#
# Напишите программу, которая получает на вход радиус случайной планеты
# и выводит на экран, во сколько раз планета Земля меньше или больше
# теоретически возможной планеты по объёму. Ответ округлите до трёх знаков после запятой.
#
# Пример 1:
# Введите радиус случайной планеты: 3389.5
# Объём планеты Земля больше в 6.641 раз
#
# Пример 2:
# Введите радиус теоретически возможной планеты: 7000
# Объём планеты Земля меньше в (1/0.754) = 1.326 раз
#
# Что оценивается
# Результат вывода соответствует условию.
# Формат вывода соответствует примеру.
# Input содержит корректное приглашение для ввода.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

import math

lAND_V = 1.08321 * 10 ** 12
lAND_R = 6371.00604465
print(f"Радиус Земли: {lAND_R} \n")


def is_exist(planet_R: float) -> bool:
    return planet_R <= 0


def compare_volume_planets(planet_R: float) -> float:
    if is_exist(planet_R):
        raise ValueError(f"Нет решения.\n")

    planet_volume = 4 * math.pi / 3 * (planet_R ** 3)

    print(f"Объем Земли {lAND_V}, объем планеты: {planet_volume}")

    if planet_volume < lAND_V:
        compare_volume = lAND_V / planet_volume
    elif planet_volume > lAND_V:
        compare_volume = planet_volume / lAND_V
    else:
        pass

    return round(compare_volume, 3)



if __name__ == '__main__':
    test_cases = [
        (6371.00604465),
        (6569.925261403126),
        (6000),
        (7000),
        (16789),
        (5.43789 * 10 ** 12),
        (0),
        (0.08321),
        (10),
        (-16789)
    ]

    for planet_R in test_cases:
        try:
            result_compare = compare_volume_planets(planet_R)
            if lAND_R > planet_R:
                print(f"Земля больше потенциальной планеты радиуса {planet_R} в {result_compare} раз.\n")
            elif lAND_R < planet_R:
                print(f"Земля меньше потенциальной планеты радиуса {planet_R} в {result_compare} раз.\n")
            else:
                print(f"Объем Земли примерно равен объему потенциальной планеты радиуса {planet_R}.\n")
        except ValueError as e:
            print(e)