# Часть 2. Модуль 7. Практическая работа. Задача 1. Ревью кода
#
# В задании был словарь из трёх студентов. Необходимо:
#
# Вывести на экран список пар «ID студента — возраст».
# Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения:
# полный список интересов всех студентов и общую длину всех фамилий студентов.
# Далее в основном коде вызывается функция, значения присваиваются отдельным переменным и выводятся на экран.
#
# Код выдает верный результат:
#
# students = {
# 1: {
# 'name': 'Bob',
# 'surname': 'Vazovski',
# 'age': 23,
# 'interests': ['biology, swimming']
# },
# 2: {
# 'name': 'Rob',
# 'surname': 'Stepanov',
# 'age': 24,
# 'interests': ['math', 'computer games', 'running']
# },
# 3: {
# 'name': 'Alexander',
# 'surname': 'Krug',
# 'age': 22,
# 'interests': ['languages', 'health food']
# }
# }
#
# def f(dict):
# lst = []
# string = ''
# for i in dict:
# lst += (dict[i]['interests'])
# string += dict[i]['surname']
# cnt = 0
# for s in string:
# cnt += 1
# return lst, cnt
#
# pairs = []
# for i in students:
# pairs += (i, students[i]['age'])
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# Перепишите этот код так, чтобы он был максимально pythonic. Убедитесь, что программа верно работает.
# Проверки на существование записей в словаре не обязательны, но приветствуются.
#
# Результат работы программы:
# Список пар «ID студента — возраст»: [(1, 23), (2, 24), (3, 22)]
# Полный список интересов всех студентов:
# {'running', 'computer games', 'math', 'languages', 'biology, swimming', 'health food'}
# Общая длина всех фамилий студентов: 20
#
# Советы и рекомендации
# Имена переменных и функций должны быть полезными и понятными
# (не стоит использовать одиночные буквы, непонятные сокращения).
# Названия не должны пересекаться с уже существующими в Python объектами
# (например, лучше не называть свою переменную print или list).
#
# Попробуйте найти лишние действия в коде. Если вы сможете получить нужный результат меньшим количеством действий,
# то не нужно заставлять Python выполнять лишние действия.
# Также нет необходимости заставлять Python выполнять одни и те же действия над одним и тем же объектом
# (например, вызывать функцию с одними и теми же входными данными несколько раз).
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d
# Новый код более оптимизирован и чист по стилю программирования (pythonic), чем старый.

students = {
    1: {'name': 'Bob', 'surname': 'Vazovski', 'age': 23, 'interests': ['biology, swimming']},
    2: {'name': 'Rob', 'surname': 'Stepanov', 'age': 24, 'interests': ['math', 'computer games', 'running']},
    3: {'name': 'Alexander', 'surname': 'Krug', 'age': 22, 'interests': ['languages', 'health food']}
}
def interests_and_length_surnames(some_dict):
    some_list = []
    length_surnames = 0

    for index in some_dict:
        some_list.append(some_dict[index]['interests'])
        length_surnames += len(some_dict[index]['surname'])

    return some_list, length_surnames


print("ID студента — возраст:")
for student in students.values():
    print(f"{student['name']} {student['surname']} - {student['age']}")

list_interests, length_surnames = interests_and_length_surnames(students)
print(f"\nПолный список интересов всех студентов:\n{list_interests}\n"
      f"\nОбщая длина всех фамилий студентов: {length_surnames}")
