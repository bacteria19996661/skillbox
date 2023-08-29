# Часть 2. Модуль 9. Практическая работа. Задача 4. Турнир
#
# В файле first_tour.txt записано число K и данные об участниках:
# фамилии, имена и количество баллов, набранных в первом туре.
# Во второй тур проходят участники, которые набрали более K баллов в первом туре.
#
# Напишите программу, которая выводит в файл second_tour.txt данные всех участников,
# прошедших во второй тур, с нумерацией.
#
# В первой строке нужно вывести в файл second_tour.txt количество участников второго тура.
# Затем программа должна вывести фамилии, инициалы и количество баллов всех участников,
# прошедших во второй тур, с нумерацией. Имя нужно сократить до одной буквы.
# Список должен быть отсортирован по убыванию набранных баллов.
#
# Пример:
# Содержимое файла first_tour.txt:
# 80
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78
#
# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
# Входные и выходные файлы названы так, как указано в задании.

with open('first_tour.txt', 'r') as first_tour:
    k = int(first_tour.readline())
    gamers_list = [line.split() for line in first_tour if int(line.split()[2]) > k]

points_list = [el[2] for el in gamers_list]
points_list.sort(reverse=True)
gamers_count = len(gamers_list)

with open('second_tour.txt', 'w') as second_tour:
    second_tour.write(str(gamers_count)+'\n')
    for i in range(gamers_count):
        for j, el in enumerate(gamers_list):
            if points_list[i] == gamers_list[j][2]:
                second_tour.write(f"{i+1}) {el[0]} {el[1][0]}. {el[2]}\n")