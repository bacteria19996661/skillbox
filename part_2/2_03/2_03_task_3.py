# Часть 2. Модуль 3. Практическая работа. Задание 3. Детали
#
# В базе данных магазина всякой всячины хранится список названий деталей и их стоимостей:
#
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
#
# Напишите программу, которая запрашивает у пользователя деталь, считает их количество и общую стоимость.
#
# Пример:
# Название детали: седло
# Количество деталей: 3
# Общая стоимость: 4500
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

shop = [
    ['каретка', 1200],
    ['шатун', 1000],
    ['седло', 300],
    ['педаль', 100],
    ['седло', 1500],
    ['рама', 12000],
    ['обод', 2000],
    ['шатун', 200],
    ['седло', 2700]
]

count = 0
summ = 0
detail = input('Введите название детали: ')

for i_shop in shop:
    if i_shop[0] == detail:
        count += 1
        summ += i_shop[1]

print(f"Кол-во деталей {count}, общая сумма: {summ}")