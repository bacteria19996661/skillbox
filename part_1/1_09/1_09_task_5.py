# Часть 1. Модуль 9. Задание 5. Великий и могучий
#
# Напишите программу, которая получает на вход текст и находит длину
# самого длинного слова в нём. Слова в тексте разделяются одним пробелом.
#
# Пример:
# Введите текст: Меня зовут Пётр.
# Самое длинное слово, букв: 5.
#
# Введите текст: Меня зовут Василий
# Самое длинное слово, 7 букв
#
# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);
# переменные имеют значащие имена, не только a, b, c, d (видео 2.3).
# Рекомендации по выполнению
# При помощи функции print убедитесь, что счётчики обнуляются в нужный момент.
# Не забывайте, что не все условия можно собирать в один условный блок.
# Некоторые из них должны срабатывать независимо друг от друга.

text = (input('\nВведите текст:\n\n'))

sub_text = text.split(' ')
length_sub_text = []

for item in sub_text:
    length_sub_text.append(len(item))

result = sub_text[int(length_sub_text.index(max(length_sub_text)))]

print(f"\nСамое длинное слово в строке - {result}\n")
