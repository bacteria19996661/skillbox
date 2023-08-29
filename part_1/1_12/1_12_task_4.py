# Часть 1. Модуль 12. Задача 4. Число наоборот
#
# Вводится последовательность чисел, оканчивающаяся нулём.
# Реализуйте функцию, которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.
#
# Пример:
# Введите число: 1234
# Число наоборот: 4321
# Введите число: 1000
# Число наоборот: 0001
# Введите число: 0
# Программа завершена!
#
# Дополнительно: добейтесь такого вывода чисел, в начале которых идут нули.
# Пример:
# Введите число: 1230
# Число наоборот: 321
#
# Ноль, который мы убрали, называется ведущим.
#
# Что оценивается
# Результат вывода соответствует условию.
# Формат вывода соответствует примеру.
# В input содержится корректное приглашение для ввода.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

def opposite_numbers(some_sequence:str):

    temp_list_numbers = []
    list_numbers = []
    new_number = ''
    for number in some_sequence:
        for i in range(0, len(number)):
            temp_list_numbers.append(number[i])
        temp_list_numbers.reverse()
        new_number = "".join(temp_list_numbers)
        list_numbers.append(str(int(new_number)))
        temp_list_numbers.clear()
    return list_numbers


if __name__ == '__main__':
    test_cases = [
        ('12345', '6789', '1080', '160', '4054', '0'),
        ('1', '0'),
        ('0'),
        ('0000', '000', '00', '0'),
        ]

    for some_sequence in test_cases:
        result_sequence = opposite_numbers(some_sequence)
        print(f"Исходная последовательность {some_sequence}:"
              f"\nПоследовательность наоборот: {result_sequence}")
