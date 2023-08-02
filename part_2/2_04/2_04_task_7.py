# Часть 2. Модуль 4. Практическая работа. Задание 7. Список списков
#
# Дан многомерный список:
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# Напишите код, который раскрывает все вложенные списки, то есть оставляет лишь внешний список.
# Для решения используйте только list comprehensions.
# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует ответу.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# мое решение
result = [z for x in range(len(nice_list)) for y in range(len(nice_list[x])) for z in nice_list[x][y]]
print(result)

# решение skillbox
# output = [digit for each_list in nice_list for each_list_2 in each_list for digit in each_list_2]
# print(output)

