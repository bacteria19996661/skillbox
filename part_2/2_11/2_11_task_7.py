# Часть 2. Модуль 11. Практическая работа. Задача 7. Матрицы
#
# Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам поручили
# разработать класс Matrix для обработки и анализа данных.
# Ваш класс должен предоставлять функциональность для выполнения основных операций с матрицами,
# таких как сложение, вычитание, умножение и транспонирование. Это будет полезно для обработки и
# структурирования больших объёмов данных, которые используются в обучении нейронных сетей.
#
# Задача
# Создайте класс Matrix для работы с матрицами.
# Реализуйте методы:
# сложения,
# вычитания,
# умножения,
# транспонирования матрицы.
# Создайте несколько экземпляров класса Matrix и протестируйте реализованные операции.
#
# Советы
# Методы сложения/вычитания/умножения должны получать параметром другую матрицу
# (объект класса Matrix) и выполнять указанное действие над своей и этой другой матрицей.
# Например, метод сложения должен получить параметром новую матрицу и сложить её со своей текущей.
# Метод транспонирования не должен ничего получать, он должен работать исключительно со своей матрицей.
# Транспонирование — это алгоритм, при котором строки матрицы меняются местами с её столбцами:
#
# Алгоритм транспонирования матрицы можно расписать следующим образом:
# Создать новую матрицу result с размерами, обратными размерам исходной матрицы.
# Количество строк новой матрицы равно количеству столбцов исходной, а количество столбцов
# новой матрицы равно количеству строк исходной.
# Пройтись по каждому элементу исходной матрицы. Для каждого элемента с индексами (i, j):
# Поместить значение этого элемента (i, j) в ячейку с индексами (j, i) новой матрицы.
# То есть транспонирование происходит с помощью обмена индексов местами.
# После завершения цикла новая матрица result будет содержать транспонированную матрицу, которую можно вернуть.
#
# Пример:
#
# # Создание экземпляров класса Matrix
# m1 = Matrix(2, 3)
# m1.data = [[1, 2, 3], [4, 5, 6]]
#
# m2 = Matrix(2, 3)
# m2.data = [[7, 8, 9], [10, 11, 12]]
#
# # Тестирование операций
# print("Матрица 1:")
# print(m1)
#
# print("Матрица 2:")
# print(m2)
#
# print("Сложение матриц:")
# print(m1.add(m2))
#
# print("Вычитание матриц:")
# print(m1.subtract(m2))
#
# m3 = Matrix(3, 2)
# m3.data = [[1, 2], [3, 4], [5, 6]]
#
# print("Умножение матриц:")
# print(m1.multiply(m3))
#
# print("Транспонирование матрицы 1:")
# print(m1.transpose())
# Вывод
# Матрица 1:
# 1    2    3
# 4    5    6
#
# Матрица 2:
# 7    8    9
# 10    11    12
#
# Сложение матриц:
# 8    10    12
# 14    16    18
#
# Вычитание матриц:
# -6    -6    -6
# -6    -6    -6
#
# Умножение матриц:
# 22    28
# 49    64
#
# Транспонирование матрицы 1:
# 1    4
# 2    5
# 3    6

import random


class Matrix:

    def __init__(self, dim_row: int = random.randint(1, 10), dim_col: int = random.randint(1, 10)):

        self.dim_col = dim_col
        self.dim_row = dim_row
        self.matrix = [[random.randint(0, 9) for _ in range(dim_col)] for _ in range(dim_row)]

    def print_matrix(self):
        for i in range(self.dim_row):
            print()
            for j in range(self.dim_col):
                print(f"{self.matrix[i][j]}", end=' \t')
        print()

    def __getitem__(self, index):
        return self.matrix[index]

    def __len__(self):
        return matrix_1.dim_row, matrix_1.dim_col

    def get_matrix(self, some_list):
        return [some_list[self.dim_col * i:self.dim_col + self.dim_col * i] for i in range(self.dim_row)]

    def __add__(self, other):
        temp_list = []
        for i in range(self.dim_row):
            for j in range(self.dim_col):
                temp_list.append(self.matrix[i][j] + other[i][j])

        return self.get_matrix(temp_list)

    def __sub__(self, other):
        temp_list = []
        for i in range(self.dim_row):
            for j in range(self.dim_col):
                temp_list.append(self.matrix[i][j] - other[i][j])

        return self.get_matrix(temp_list)

    def __mul__(self, other):
        temp_list = []
        for i in range(self.dim_row):
            for j in range(self.dim_col):
                temp_list.append(self.matrix[i][j] * other[i][j])

        return self.get_matrix(temp_list)

    def transpon(self):
        temp_list = []
        for j in range(self.dim_col):
            for i in range(self.dim_row):
                temp_list.append(self.matrix[i][j])

        return [temp_list[self.dim_row * i:self.dim_row + self.dim_row * i] for i in range(self.dim_col)]


def print_matrix(some_matrix):
    n = matrix_1.__len__()
    for i in range(n[0]):
        print()
        for j in range(n[1]):
            print(f"{some_matrix[i][j]}", end=' \t')
    print()


def print_transpon(some_matrix):
    n = matrix_1.__len__()
    for i in range(n[1]):
        print()
        for j in range(n[0]):
            print(f"{some_matrix[i][j]}", end=' \t')
    print()


if __name__ == '__main__':
    matrix_1 = Matrix()
    matrix_2 = Matrix()
    print("\nМатрица А:")
    matrix_1.print_matrix()
    print("\nМатрица B:")
    matrix_2.print_matrix()

    print("\nМатрица A+B:")
    result_add = matrix_1.__add__(matrix_2)
    print_matrix(result_add)

    print("\nМатрица A-B:")
    result_sub = matrix_1.__sub__(matrix_2)
    print_matrix(result_sub)

    print("\nМатрица A*B:")
    result_mul = matrix_1.__mul__(matrix_2)
    print_matrix(result_mul)

    print("\nТранспонированная матрица A:")
    result_trans = matrix_1.transpon()
    print_transpon(result_trans)
