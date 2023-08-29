# Часть 1. Модуль 13. Задача 4. Недоделка 2
#
# Программа получает на вход два числа;
# в первом числе должно быть не менее трёх цифр,
# во втором — не менее четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то
# в каждом числе первая и последняя цифры меняются местами,
# а затем выводится их сумма.
#
# Повторений кода должно быть как можно меньше.
# Также сделайте, чтобы в основной части программы был только ввод чисел,
# затем изменённые числа и вывод их суммы.
#
# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя,
# выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи
# (проверки и изменения двух чисел).
#
# Что оценивается
# Программа разбита на несколько функций.
# Выполнены условия по организации основного тела программы.

def count_numbers(number: int):

    num_count = 0
    temp_number = number

    while temp_number > 0:
        num_count += 1
        temp_number = temp_number // 10

    return num_count


def change_number(number: int):
    num_count = count_numbers(number)

    last_digit = number % 10
    first_digit = number // 10 ** (num_count - 1)
    between_digits = number % 10 ** (num_count - 1) // 10
    number = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit

    return number


def main():

    first_n = int(input("Введите первое число: "))
    count_numbers(first_n)
    if count_numbers(first_n) < 3:
        return print(f"В числе меньше трёх цифр.")
    else:
        first_result = change_number(first_n)
        print(f"Изменённое первое число: {first_result}")

    second_n = int(input("\nВведите второе число: "))
    count_numbers(second_n)
    if count_numbers(second_n) < 4:
        return print(f"В числе меньше четырёх цифр.")
    else:
        second_result = change_number(second_n)
        print(f"Изменённое второе число: {second_result}")

    print(f"\nСумма чисел: {first_result + second_result}")


main()
