# Модуль 12. Задача 5. Текстовый редактор
#
# Напишите функцию count_letters(), которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N. Функция должна вывести на экран
# информацию о найденных буквах и цифрах в определённом формате.
#
# Пример:
#
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? Л
#
# Количество цифр 0: 2
# Количество букв Л: 1
#
# Что оценивается
# Результат вывода соответствует условию.
# В input содержится корректное приглашение для ввода.
# Формат вывода соответствует примеру.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).


def count_symbols(text: str):
    print(text)
    letter = str(input('Введите букву, которую будем считать: '))
    finger = str(input('Введите цифру, которую будем считать: '))
    letter = letter.lower()
    text = text.lower()

    count_letter, count_finger = 0, 0

    for symbol in text:
        if symbol == letter:
            count_letter += 1
        if symbol == finger:
            count_finger += 1
    return count_letter, count_finger



if __name__ == '__main__':
    test_cases = [
        ('100 Лет в Обед'),
        ('Когда 100 лет? Кому обед, а кому котлет?'),
        ('   @   '),
        (''),
        ]

    for text in test_cases:
        result = count_symbols(text)
        print(f"(букв, цифр) = {result}\n")
