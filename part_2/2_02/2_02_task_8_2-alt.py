# Часть 2. Модуль 2. Практическая работа. Задание 8. Сортировка
#
# Написать наиболее эффективный алгоритм сортировки.


import random
import time


start_creating_list = time.perf_counter()
def creating_list(minnumber, maxnumber, quantity):
    rand_list = []

    for _ in range(quantity):
       rand_list.append(random.randint(minnumber, maxnumber))

    return rand_list
creating_list_speed = time.perf_counter() - start_creating_list
print(f"Скорость генерации списка: {creating_list_speed}\n")




# Сортировка пузырьком (bubble sort) — простой алгоритм сортировки,
# который проходит по списку несколько раз, сравнивая пары соседних элементов
# и меняя их местами, если они находятся в неправильном порядке.
# Этот процесс повторяется до тех пор, пока весь список не будет отсортирован.

start_bubble_sort = time.perf_counter()
def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Сравниваем пару соседних элементов
            if lst[j] > lst[j + 1]:
                # Если элементы находятся в неправильном порядке, меняем их местами
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
bubble_sort_speed = time.perf_counter() - start_bubble_sort
print(f"Скорость сортировки пузырьком: {bubble_sort_speed}")




# Сортировка вставками (insertion sort) — простой алгоритм сортировки,
# который постепенно строит отсортированную последовательность, один элемент за другим,
# вставляя каждый новый элемент в правильное место.

start_insertion_sort = time.perf_counter()
def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]  # Берём текущий элемент, который нужно вставить в отсортированную часть списка
        j = i - 1
        # Перемещаем элементы, которые больше key, на одну позицию вперёд
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key  # Вставляем key в правильное место
    return lst
insertion_sort_speed = time.perf_counter() - start_insertion_sort
print(f"Скорость сортировки вставками: {insertion_sort_speed}")




# Сортировка Шелла (Shell sort) — применяет сортировку вставками к диапазонам элементов с определённым шагом.
# Шаг постепенно уменьшается, позволяя элементам быстрее перемещаться в свои конечные позиции.
# Таким образом, сортировка Шелла — это усовершенствованный вариант сортировки вставками.
# Универсальный

start_shell_sort = time.perf_counter()
def shell_sort(lst):
    n = len(lst)
    gap = n // 2  # Инициализация начального значения интервала

    while gap > 0:
        # Применяем сортировку вставками с заданным интервалом
        for i in range(gap, n):
            temp = lst[i]
            j = i
            # Сдвигаем элементы, чтобы найти правильную позицию для вставки элемента
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2  # Уменьшаем интервал

    return lst
shell_sort_speed = time.perf_counter() - start_shell_sort
print(f"Скорость сортировки Шелла: {shell_sort_speed}")




# Сортировка выбором (selection sort) — на каждом шаге находит минимальный или максимальный элемент
# из неотсортированной части списка и помещает его в начало или конец отсортированной части.
# Устойчивый, ограниченно эффективен.

start_selection_sort = time.perf_counter()
def selection_sort(lst):
    n = len(lst)

    for i in range(n - 1):
        min_index = i
        # Находим индекс минимального элемента в неотсортированной части списка
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        # Меняем местами минимальный элемент с первым элементом неотсортированной части
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst
selection_sort_speed = time.perf_counter() - start_selection_sort
print(f"Скорость сортировки выбором: {selection_sort_speed}")




# Сортировка слиянием (merge sort) — использует стратегию «разделяй и властвуй».
# Он разбивает список на две половины, рекурсивно сортирует каждую, затем объединяет их.
# Для работы с большим объемом данных

start_merge_sort = time.perf_counter()
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    # Разделяем список на две половины
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    # Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # Объединяем отсортированные половины в один список
    return merge_2(left_half, right_half)

def merge_2(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        # Сравниваем элементы из обоих списков и добавляем меньший в объединённый список
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Добавляем оставшиеся элементы из левого списка
    merged.extend(left[left_index:])
    # Добавляем оставшиеся элементы из правого списка
    merged.extend(right[right_index:])
    return merged
merge_sort_speed = time.perf_counter() - start_merge_sort
print(f"Скорость сортировки слиянием: {merge_sort_speed}")




# Timsort — гибридный алгоритм, который комбинирует идеи из сортировки слиянием (merge sort)
# и сортировки вставками (insertion sort) для достижения эффективности в разных сценариях сортировки,
# при этом он сохраняет относительный порядок равных элементов.
# Timsort — адаптивный алгоритм, который оптимизирован для разных случаев,
# включая частично отсортированные или обратно отсортированные списки.
# Он эффективно обрабатывает списки с повторяющимися элементами.

start_timsort = time.perf_counter()
minrun = 32
def InsSort(arr, start, end):
    for i in range(start + 1, end + 1):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr

def merge(arr, start, mid, end):
    if mid == end:
        return arr
    first = arr[start:mid + 1]
    last = arr[mid + 1:end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < len1 and ind2 < len2:
        if first[ind1] < last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1 < len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2 < len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr

def TimSort(arr):
    n = len(arr)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        arr = InsSort(arr, start, end)

    curr_size = minrun
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            arr = merge(arr, start, mid, end)
        curr_size *= 2
    return arr
timSort_speed = time.perf_counter() - start_timsort
print(f"Скорость сортировки Timsort: {timSort_speed}")




if __name__ == '__main__':
    rand_list = creating_list(-1000, 1000, 10**5)

    print(f"\nРандомизированный список:\n{rand_list}\n")
    # print(f"nАлгоритм сортировки пузырьком:\n{bubble_sort(rand_list)}"
          # f"\nАлгоритм сортировки вставками:\n{insertion_sort(rand_list)}"
          # f"\nАлгоритм сортировки Шелла:\n{shell_sort(rand_list)}"
          # f"\nАлгоритм сортировки выбором:\n{selection_sort(rand_list)}"
          # f"\nАлгоритм сортировки слиянием:\n{merge_sort(rand_list)}"
          # f"\nАлгоритм сортировки TimSort:\n{TimSort(rand_list)}")

    dict = {
        bubble_sort_speed: 'Пузырьком',
        insertion_sort_speed: 'Вставками',
        shell_sort_speed: 'Шелла',
        selection_sort_speed: 'Выбором',
        merge_sort_speed: 'Слиянием',
        timSort_speed: 'TimSort'
    }
    speed_list = [bubble_sort_speed, insertion_sort_speed, shell_sort_speed,
                  selection_sort_speed, merge_sort_speed, timSort_speed]
    speed_list.sort()

    print('Скорость сортировки алгоритмов (от быстрой к медленной):\n')
    for elem in speed_list:
        print(f"{dict.setdefault(elem)} speed = {elem}")
