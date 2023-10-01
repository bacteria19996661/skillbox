#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 13. Практическая работа. Задача 4. Реализовать ОДНОСВЯЗНЫЙ СПИСОК
#
# Связный список — это структура данных, которая состоит из элементов, называющихся узлами.
# В узлах хранятся данные, а между собой узлы соединены связями. Связь — это ссылка на следующий
# или предыдущий элемент списка.
#
# В односвязном списке связь — это ссылка только на следующий элемент, то есть в нём можно
# передвигаться только в сторону конца списка. Узнать адрес предыдущего элемента,
# опираясь на содержимое текущего узла, невозможно.
#
# Реализуйте такую структуру данных без использования стандартных структур Python
# (list, dict, tuple и прочие) и дополнительных модулей.
#
# Для реализации напишите два класса: Node и LinkedList. В Node должна быть логика
# работы одного узла (хранение данных и указателя).
#
# Для структуры реализуйте следующие методы:
#
# append — добавление элемента в конец списка;
# get — получение элемента по индексу;
# remove — удаление элемента по индексу.
# Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла.
#
# Пример основной программы:
# my_list = LinkedList()
# my_list.append(10)
# my_list.append(20)
# my_list.append(30)
# print('Текущий список:', my_list)
# print('Получение третьего элемента:', my_list.get(2))
# print('Удаление второго элемента.')
# my_list.remove(1)
# print('Новый список:', my_list)
#
# Результат:
# Текущий список: [10 20 30]
# Получение третьего элемента: 30
# Удаление второго элемента.
# Новый список: [10 30]
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
# Для создания нового класса на основе уже существующего используется наследование.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs).
# Если функция/метод ничего не возвращает, то используется None.

class Node:    # логика работы одного узла
    def __init__(self, data=None, link=None):
        self.data = data    # Значение узла
        self.link = link    # Ссылка на следующий узел

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_link(self):
        return self.link

    def set_link(self, link):
        self.link = link

    def __str__(self):
        return '{}'.format(self.data)


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def append_begin(self, data):
        node = Node(data, self.head)
        self.head = node
        # print('В начало списка добавлен новый элемент {}.'.format(self.head))

    def append_end(self, data):
        new_node = Node(data)
        # print('Добавлен новый элемент в конец списка: {}.'.format(new_node))
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.get_link():
            current_node = current_node.get_link()

        current_node.link = new_node

    def get(self, value):    # получение элемента
        current_node = self.head
        while current_node:
            if current_node.get_data() == value:
                print('Элемент {} найден.'.format(current_node.get_data()))
                return current_node.get_data()
            else:
                current_node = current_node.get_link()
        print('Элемент {} не найден.'.format(value))
        return None

    def get_by_index(self, index):
        current_node = self.head
        position = 0
        if position == index:
            print('{} (id = {})'.format(current_node.get_data(), index))
            return current_node.get_data()
        else:
            while (current_node != None and position != index):
                position += 1
                current_node = current_node.get_link()
            if current_node != None:
                print('{} (id = {})'.format(current_node.get_data(), index))
                return current_node.get_data()
            else:
                print("Такого индекса нет")

    def remove(self, value):    # удаление элемента по значению
        prev = None    # предыдущий
        current_node = self.head    # текущий
        while current_node:
            if current_node.get_data() == value:    # если значение совпадает с текущим, то
                if prev:    # если предыдущий
                    prev.set_link(current_node.get_link())
                else:
                    self.head = current_node.get_link()
                print('Элемент {} удален.'.format(current_node.get_data()))
                return current_node.get_data()

            prev = current_node
            current_node = current_node.get_link()

        return False

    def remove_first_node(self):
        if self.head == None:
            return None
        self.head = self.head.get_link()

    def remove_by_index(self, index):
        if self.head == None:
            return None

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while (current_node != None and position + 1 != index):
                position += 1
                current_node = current_node.get_link()

            if current_node != None:
                print('{} (id = {})'.format(current_node.link, index))
                current_node.link = current_node.link.get_link()

            else:
                print("Нет такого индекса!")

    def print_data(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.get_link()
        print()


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append_end(10)
    my_list.append_end(20)
    my_list.append_end(30)
    print('Текущий список:', end=' ')
    my_list.print_data()
    print('Получение элемента:', end=' ')
    my_list.get_by_index(2)
    print('Удаление элемента:', end=' ')
    my_list.remove_by_index(1)
    print('Новый список:', end=' ')
    my_list.print_data()
