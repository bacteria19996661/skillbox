# Часть 2. Модуль 4. Практическая работа. Задание 1. Гласные буквы
#
# Напишите программу, которая запрашивает у пользователя текст и генерирует список гласных букв
# этого материала (сама строка вводится на русском языке). Выведите в консоль сам список и его длину.
#
# Пример:
# Введите текст: Нужно отнести кольцо в Мордор!
# Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
# Длина списка: 9
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

a_str = 'АаЕеЁёИиОоУуЫыЭэЮюЯя'
text = input('Введите текст: ')

list_a = [i_text for i_text in text if i_text in a_str]

print(f"Список гласных букв: {list_a}\n"
      f"Длина списка: {len(list_a)}")

