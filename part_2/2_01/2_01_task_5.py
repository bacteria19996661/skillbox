# 5. Годы
#
# Напишите программу, в которой у пользователя запрашиваются два четырёхзначных числа A и B.
# Затем выведите в порядке возрастания все четырёхзначные числа в интервале от A до B,
# запись которых содержит ровно три одинаковые цифры.
#
# Пример
# Введите первый год: 1900
# Введите второй год: 2100
# Годы от 1900 до 2100 с тремя одинаковыми цифрами:
# 1911
# 1999
# 2000
# 2022
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельной(-ых) функции(-ях).
# Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).


def is_correct(year: str) -> bool:
    return len(year) != 4 or not(str(year).isdigit()) or int(year) < 0


def three_identical_digits(year: str):
    if is_correct(str(year)):
        raise ValueError(f"Ошибка ввода. Введите четырехзначное натуральное число.")

    year = str(year)
    a = year[3]
    if ((a == year[0] and a == year[1]) or (a == year[0] and a == year[2]) or (a == year[1] and a == year[2])) \
            and ((a != year[0]) or (a != year[1]) or (a != year[2])):
        print(year)


def years_list(year1, year2):

    for year in range(int(year1), int(year2) + 1):
        three_identical_digits(str(year))



if __name__ == '__main__':
    year1 = int(input('Введите начальный год: '))
    year2 = int(input('Введите конечный год: '))
    if year1 > year2:
        year1, year2 = year2, year1

    try:
        if is_correct(str(year1)) == False and is_correct(str(year1)) == False:
            print('Годы с тремя одинаковыми цифрами:')

        result = years_list(year1, year2)

    except ValueError as e:
        print(e)
