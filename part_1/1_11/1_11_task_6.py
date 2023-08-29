# Часть 1. Модуль 11. Задача 6. Ход конём
#
# В рамках разработки шахматного ИИ стоит новая задача: по заданным вещественным координатам коня
# и точки программа должна определить, может ли конь ходить в эту точку.
# Используйте как можно меньше конструкций if и логических операторов. Обеспечьте контроль ввода.
#
# Пример:
# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.
#
# Что оценивается
# Результат вывода соответствует условию.
# Формат вывода соответствует примеру.
# Input содержит корректное приглашение для ввода.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

def is_exist(horse_x: float, horse_y: float, point_x: float, point_y: float) -> bool:
    return not(0 <= horse_x < 0.8 and 0 <= horse_y < 0.8 and 0 <= point_x < 0.8 and 0 <= point_y < 0.8)  # исключение


def location(horse_x: float, horse_y: float, point_x: float, point_y: float):
    if is_exist(horse_x, horse_y, point_x, point_y):
        raise ValueError(f"\nВы ввели несуществующие координаты.")

    cell_horse_x = int(horse_x * 10)
    cell_horse_y = int(horse_y * 10)

    cell_point_x = int(point_x * 10)
    cell_point_y = int(point_y * 10)

    print(f"\nКонь в клетке ({cell_horse_x}, {cell_horse_y}). Точка в клетке ({cell_point_x}, {cell_point_y}).")

    if ((cell_horse_x == cell_point_x + 1 and cell_horse_y == cell_point_y + 2) or (
        cell_horse_x == cell_point_x + 2 and cell_horse_y == cell_point_y + 1) or (
        cell_horse_x == cell_point_x + 1 and cell_horse_y == cell_point_y - 2) or (
        cell_horse_x == cell_point_x + 2 and cell_horse_y == cell_point_y - 1) or (
        cell_horse_x == cell_point_x - 1 and cell_horse_y == cell_point_y + 2) or (
        cell_horse_x == cell_point_x - 2 and cell_horse_y == cell_point_y + 1) or (
        cell_horse_x == cell_point_x - 1 and cell_horse_y == cell_point_y - 2) or (
        cell_horse_x == cell_point_x - 2 and cell_horse_y == cell_point_y - 1)):
        print('Да, конь может ходить в эту точку.')
    else:
        print('Конь не может ходить в эту точку.')


if __name__ == '__main__':
    test_cases = [
        (0.071, 0.118, 0.213, 0.068),
        (0.345, 0.789, 0.415, 0.602),
        (0.65, 0.89, 0.21, 0.531),
        (0, 0, 0.2, 0.1),
        (1.0, 1.0, 1, 1),
        (-0.1, 0.3, 0.5, 0.7),
    ]

    for horse_x, horse_y, point_x, point_y in test_cases:
        try:
            location(horse_x, horse_y, point_x, point_y)

        except ValueError as e:
            print(e)
