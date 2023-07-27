# Часть 2. Модуль 2. Практическая работа. Задание 2. Уникальное объединение списков
#
# Напишите программу, которая объединяет два отсортированных списка целых чисел в один отсортированный список без дубликатов.
#
# Пример:
# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
# merged = merge_sorted_lists(list1, list2)
# print(merged)
# Вывод в консоли:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Советы
# Учтите, что один список может быть короче другого.
# Проверьте ваше решение с различными тестовыми данными, включая случаи с пустыми списками,
# списками без дубликатов и списками с повторяющимися элементами.
# Убедитесь, что в вашем итоговом списке не будет дубликатов.


def merge_sorted_lists(list1, list2):
    print(f"Исходные списки:\n{list1}\n{list2}")
    list1.extend(list2)
    print(f"Слияние:{list1}")
    list1.sort()
    print(f"Сортировка:{list1}")
    set_list = set(list1)
    list1 = list(set_list)

    return list1

if __name__ == '__main__':
    test_cases = [
        [[1, 3, 5, 7, 9], [2, 4, 5, 6, 8, 10]],
        [[1, 3, 5, 7, 9], [2, 4, 6, 8]],
        [[1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 5, 7, 8, 9]],
        [[1, 3, 5, 7, 9], [1, 3, 5, 7, 9]],
        [[1, 3, 5, 7, 9], []],
        [[], []]
    ]

    for list1, list2 in test_cases:
        result = merge_sorted_lists(list1, list2)
        print(f"Слитый отсортированный и очищенный от дубликатов список:\n{result}\n")