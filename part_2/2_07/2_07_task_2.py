# Часть 2. Модуль 7. Практическая работа. Задача 2. Универсальная программа
#
# Напишите функцию, возвращающую список элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс — это простое число.
#
# Для проверки на простое число напишите отдельную функцию is_prime.
#
# Необязательное усложнение: сделайте так, чтобы основная функция состояла только из оператора return
# и так же возвращала список.
#
# Пример вызова функции:
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# Ответ в консоли: [2, 3, 5, 7]
# Пример вызова функции:
# print(crypto('О Дивный Новый мир!'))
# Ответ в консоли: ['Д', 'и', 'н', 'й', 'в', 'й', 'р']
#
# Советы и рекомендации
# Для нумерации элементов используйте функцию enumerate. Это позволит работать одинаково со всеми структурами данных.
#
# Что оценивается
# Результат вычислений корректен.
# Весь функционал программы описан в функциях.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

import random
def is_prime(num):

    flag = False
    for k in range(2, num):
        if num % k == 0:
            flag = True

    if flag == True:
        return False
    else:
        return True

def elem_from_prime(some_object):
    if isinstance(some_object, dict):
        list_elem_from_prime = [val for key, val in some_object.items() if is_prime(key) and key >= 2]
    else:
        list_elem_from_prime = [el for i, el in enumerate(some_object) if is_prime(i) and i >= 2]
    return list_elem_from_prime

if __name__ == '__main__':
    test_cases = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e', 'f'),
        'О Дивный Новый мир!',
        {0: 'О', 1: ' ', 2: 'Д', 3: 'и', 4: 'в', 5: 'н', 6: 'ы', 7: 'й', 8: ' ', 9: 'Н', 10: 'о'}
    ]

    for some_object in test_cases:
        result = elem_from_prime(some_object)
        print(result)





