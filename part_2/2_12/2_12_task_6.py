#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 12. Практическая работа. Задача 6. Абстрактный класс
#
# Вы работаете в компании, занимающейся разработкой программного обеспечения для архитектурных проектов.
# Вам необходимо разработать программу для расчёта площади различных геометрических фигур,
# таких как круги, прямоугольники и треугольники.
#
# Задача
# Создайте:
# класс Shape, который будет базовым классом для всех фигур и будет хранить пустой метод area,
# который наследники должны переопределить;
# класс Circle;
# класс Rectangle;
# класс Triangle.
# Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод для вычисления площади фигуры.
#
# Дополнительно: изучите информацию о работе с абстрактными классами.
# На основе этой информации сделайте так, чтобы:
# Нельзя было создавать объекты класса Shape.
# Наследники класса Shape переопределяли его метод area, чтобы объекты этих классов можно было использовать.

import math


class Shape:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.s = 0
        pass

    def __str__(self):
        return '{}:.2f'.format(self.s)

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, a):
        super().__init__(a, b=0, c=0)

    def area(self):
        self.s = math.pi * self.a**2
        return self.s


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(a, b, c=0)

    def area(self):
        self.s = self.a * self.b
        return self.s


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def area(self):
        p = (self.a + self.b + self.c) / 2
        self.s = math.sqrt(p*(p - self.a)*(p - self.a)*(p - self.a))
        return self.s


if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(3, 4)
    triangle = Triangle(3, 4, 5)

    circle.area()
    print(circle)
    rectangle.area()
    print(rectangle)
    triangle.area()
    print(triangle)
