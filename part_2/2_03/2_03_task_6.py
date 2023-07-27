# Часть 2. Модуль 3. Практическая работа. Задание 6. Ролики
#
# Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей.
# Реализуйте код, который определяет,
# какое наибольшее число человек может одновременно взять ролики и пойти кататься.
#
# Пример:
# Количество коньков: 4
# Размер пары 1: 41
# Размер пары 2: 40
# Размер пары 3: 39
# Размер пары 4: 42
# Количество людей: 3
# Размер ноги человека 1: 42
# Размер ноги человека 2: 41
# Размер ноги человека 3: 42
# Наибольшее количество людей, которые могут взять ролики: 2
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.
# Советы и рекомендации
# Помните, по условиям задачи размер коньков должен быть больше размера ноги или равен размеру ноги.
# Чтобы подобрать максимальное количество пар,
# старайтесь найти наименьший возможный размер коньков для каждого размера ноги.

skates_size, people_size = [], []

n = int(input('Введите кол-во пар коньков: '))
for i in range(1, n+1):
    men = int(input(f"Размеры {i}-й пары: "))
    skates_size.append(men)

k = int(input('\nВведите кол-во людей: '))
for i in range(1, k+1):
    skate = int(input(f"Размер ноги {i}-го человека: "))
    people_size.append(skate)

count = 0
for i_men in people_size:
    for j_skate in skates_size:
        if i_men == j_skate:
            skates_size.remove(j_skate)
            count += 1

print(f"\nКол-во обутых людей: {count}")
print(f"Оставшиеся размеры: {skates_size}")

