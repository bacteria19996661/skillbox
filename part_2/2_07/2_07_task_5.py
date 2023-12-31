# Часть 2. Модуль 7. Практическая работа. Задача 5. Функция сортировки
#
# Напишите функцию, которая сортирует по возрастанию кортеж, состоящий из целых чисел,
# и возвращает его отсортированным. Если хотя бы один элемент не является целым числом,
# то функция возвращает исходный кортеж.
# Основной код оставьте пустым или закомментированным (используйте его только для тестирования).
#
# Пример вызова функции:
# tpl = (6, 3, -1, 8, 4, 10, -5)
# print(tpl_sort(tpl))
# Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)
#
# Что оценивается
# Результат вычислений корректен.
# Весь функционал программы описан в виде функции.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

def tpl_sort(tpl):
    return tuple(sorted(list(tpl)))

if __name__ == '__main__':
    test_cases = [
        (6, 3, -1, 8, 4, 10, -5)
    ]

    for tpl in test_cases:
        print(tpl_sort(tpl))