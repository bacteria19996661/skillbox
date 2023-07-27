# Часть 2. Модуль 2. Практическая работа. Задача 5. Песни
#
# Есть список из девяти песен группы Depeche Mode.
# В информацию о каждом треке входит название и продолжительность с точностью до долей минут:
#
# violator_songs = [
# ['World in My Eyes', 4,86],
# ['Sweetest Perfection', 4,43],
# ['Personal Jesus', 4,56],
# ['Halo', 4,9],
# ['Waiting for the Night', 6,07],
# ['Enjoy the Silence', 4,20],
# ['Policy of Truth', 4,76],
# ['Blue Dress', 4,29],
# ['Clean', 5,83]
# ]
#
# Напишите программу, которая запрашивает у пользователя количество песен из списка и их названия,
# а на экран выводит общее время их звучания.
#
# Пример:
# Сколько песен выбрать? 3
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean
# Общее время звучания песен — 14,93 минуты
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

n = int(input('Сколько песен выбрать?: '))
timer = 0

for i in range(1, n+1):
    some_song = input(f"Название {i}-й песни: ")
    for i_song in violator_songs:
        if i_song[0] == some_song:
            timer += i_song[1]


print(f"\nОбщее время звучания песен: {round(timer, 2)} минут.")