# Часть 1. Модуль 9. Задание 2. Кривой мессенджер
#
# Напишите программу, которая определяет порядковый номер звёздочки в строке.
#
# Пример:
# Введите текст: «Пр*ивет как дела».
# Символ «*» стоит на позиции 3.
#
# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);
# переменные имеют значащие имена, не только a, b, c, d (видео 2.3).

need_symbol = '*'
word = input('Введите слово: ')

count = 1

for symbol in word:
    if symbol != need_symbol:
        count += 1
    else:
        print(f"\nСимвол «*» стоит на позиции {count} \n")
        break
