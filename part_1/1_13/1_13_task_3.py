# Модуль 13. Задача 3. Число наоборот 2
#
# Пользователь вводит два числа: N и K. Напишите программу,
# которая заменяет каждое число на число, которое получается из исходного
# записью его цифр в обратном порядке, затем складывает их,
# снова переворачивает и выводит ответ на экран.
#
# Пример:
# Введите первое число: 102
# Введите второе число: 123
# Первое число наоборот: 201
# Второе число наоборот: 321
# Сумма: 522
# Сумма наоборот: 225
#
# Что оценивается
# Результат вывода соответствует условию.
# Input содержит корректное приглашение для ввода.
# Формат вывода соответствует примеру.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).


def flip_number_reverse_order(str_number: str) -> int:
    reverse_str_number = ''
    for i in range(1, len(str_number) + 1):
        reverse_str_number += str_number[-i]
    return int(reverse_str_number)



if __name__ == '__main__':
    num1 = input("Введите первое число: ")
    reverse_mum1 = flip_number_reverse_order(str(num1))
    print(f"Число наоборот: {reverse_mum1}\n")

    num2 = input("Введите второе число: ")
    reverse_mum2 = flip_number_reverse_order(str(num2))
    print(f"Число наоборот: {reverse_mum2}\n")

    sum_numbers = reverse_mum1 + reverse_mum2

    print(f"Сумма чисел, записанных наоборот: {sum_numbers}")
    print(f"Перевернутая сумма: {flip_number_reverse_order(str(sum_numbers))}")

