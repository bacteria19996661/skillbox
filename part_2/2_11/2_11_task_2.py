# Часть 2. Модуль 11. Практическая работа. Задача 2. Студенты
#
# Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя)
# и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# Сообщения о процессе получения результата осмысленны и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.

import random
import string


class Student:

    def __init__(self, name, number, grade):
        self.name = name
        self.number = number
        self.grade = grade

    def student_info(self):
        return self.name, self.number, self.grade, sum(self.grade) / len(self.grade)


def sort_list(some_list):
    for id_min in range(len(some_list)):
        for id_temp in range(id_min, len(some_list)):
            if some_list[id_temp][3] < some_list[id_min][3]:
                some_list[id_temp], some_list[id_min] = some_list[id_min], some_list[id_temp]

    return some_list


def gen_students():
    student_list = []
    for _ in range(1, 11):
        random_string = ''.join([random.choice(string.ascii_lowercase) for _ in range(random.randint(4, 12))])
        student_name = f"{random_string.title()} {random_string.title()}"
        number = random.randint(1, 2)
        grade = tuple([random.randint(2, 5) for _ in range(5)])
        student = Student(student_name, number, grade)
        student_list.append(student.student_info())
    return student_list


if __name__ == '__main__':
    temp_list = gen_students()
    for el in sort_list(temp_list):
        print("ФИ: {}\nНомер группы: {}\nУспеваемость: {}\nСредний балл: {}\n".format(el[0], el[1], el[2], el[3]))
