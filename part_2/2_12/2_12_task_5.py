#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 12. Практическая работа. Задача 5. Стек
#
# Стек — это абстрактный тип данных, представляющий собой список элементов, организованных
# по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
#
# Напишите класс, который реализует стек и его возможности (достаточно будет добавления и удаления элемента).
#
# После этого напишите ещё один класс — «Менеджер задач». В менеджере задач можно выполнить
# команду «новая задача», в которую передаётся сама задача (str) и её приоритет (int).
# Сам менеджер работает на основе стека (не наследование). При выводе менеджера в консоль
# все задачи должны быть отсортированы по следующему приоритету: чем меньше число, тем выше задача.
#
# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать ДЗ", 2)
# print(manager)
#
# Результат:
# 1 — отдохнуть
# 2 — поесть; сдать ДЗ
# 4 — сделать уборку; помыть посуду
#
# Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами.
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
# Для создания нового класса на основе уже существующего используется наследование.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена, а не a, b, c, d.
# Классы и методы/функции имеют прописанную документацию.


class Stack:
    """
    Реаизует добавление и удаление элемента.
    """
    def __init__(self):
        self.__list = []

    def __str__(self):
        return str(", ".join(self.__list))

    def get_list(self):
        return self.__list

    def add(self, some_task):
        return self.__list.append(some_task)

    def pop(self):
        if len(self.__list) == 0:
            return None
        return self.__list.pop()


class TaskManager:
    """
    Класс «Менеджер задач» на основе стека (не наследование),
    где можно выполнить команду «новая задача»,
    в которую передаётся сама задача (str) и её приоритет (int).
    При выводе менеджера в консоль задачи отсортированы по возрастанию.

    Дополнительно: удаление задач и обработка дубликатов.
    """
    def __init__(self):
        self.task = {}

    def __str__(self):
        all_task = ""
        for i_task in sorted(self.task.keys()):    # сортировка по приоритету
            all_task += str(i_task) + " " + str(self.task[i_task]) + "\n"
        return all_task

    def new_task(self, task, priority):
        if not priority in self.task.keys():     # если задачи с таким приоритетом в ключах нет
            self.task[priority] = Stack()     # значение соваря определяется как экземпляр класса Stack
            self.task[priority].add(task)     # то задача добавляется в стек (список)
        else:    # если задача с таким приоритетом есть в ключах
            duble_stack = Stack()    # задаем новый экземпляр касса Stack для перечисления значений дубликатов приоритета
            while len(str(self.task[priority])) != 0:    # пока задачи (значения) не закончились
                value = self.task[priority].pop()    # удаляем их из обычного стека (списка) с записью возвращаемого значения
                if value != task:     # для дубюрующихся приоритетов (если удаляемая задача не совпадает с проверяемым,
                    duble_stack.add(value)    # то добавяем значение в специальный стек для дублей

            duble_stack.add(task)     # добавляем задачу с дублируемым приоритетом в специаьный стек для дубей список)
            print(f"new_stack = {duble_stack}")
            self.task[priority] = duble_stack    # добавяем значения дублей приоритета в словарь
            print(f"task = {task}")

    def delete_task(self, priority):
        if not priority in self.task.keys():    # если задачи с таким приоритетом в ключах нет
            print("Задачи с таким приоритетом нет!")
        else:
            print(f"Удалили задачу '{self.task[priority].pop()}'")
            if len(str(self.task[priority])) == 0:    # если задача удалена
                self.task.pop(priority)    # удаляем также её приоритет


# def menu():
#     manager = TaskManager()
#
#     usr_choice_command = input('Выберите действие:\n'
#                                'add - добавить задачу\n'
#                                'del - удалить задачу:\n'
#                                'exit - завершить работу:\n'
#                                'Ваш выбор: ')
#
#     if usr_choice_command == 'add':
#         flag = '1'
#         while flag == '1':
#             usr_task = input('Введите задачу: ')
#             usr_priority = int(input('Задайте приоритет: '))
#             manager.new_task(usr_task, usr_priority)
#
#             flag = input('Добавить еще задачу? 1 - да, 0 - нет. Ваш выбор: ')
#             if flag == '0':
#                 print(manager)
#                 manager.delete_task(1)
#                 manager.delete_task(4)
#                 print(manager)
#                 break
#
#     if usr_choice_command == 'del':
#         flag = '1'
#         while flag == '1':
#             usr_number = int(input('Введите номер задачи, которую нужно удалить: '))
#             manager.delete_task(usr_number)
#             print(manager)
#
#             flag = input('Добавить еще задачу? 1 - да, 0 - нет. Ваш выбор: ')
#             if flag == '0':
#                 print(manager)
#                 break
#
#     if usr_choice_command == 'exit':
#         exit()
#     else:
#         menu()

if __name__ == '__main__':
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)
    print(manager)
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 3)
    manager.new_task("сделать уборку", 4)
    print(manager)
    manager.delete_task(1)
    manager.delete_task(4)
    print(manager)
