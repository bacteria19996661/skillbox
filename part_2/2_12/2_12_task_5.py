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
    def __init__(self):
        self.__st = []

    def __str__(self):
        return '; '.join(self.__st)
        # return str(self.__st)

    def push(self, elem):
        return self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append('{priority} {task}\n'.format( priority=str(i_priority), task = self.task[i_priority]))
        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:  # если такого ключа в словаре нет,
            self.task[priority] = Stack()  # создаем пару ключ - Stack
            # т.к. значением ключа является стек, то для добавления в него элемента нужно вызвать метод push
        self.task[priority].push(task)


if __name__ == '__main__':

    # my_st = Stack()
    # for i in range(5):
    #     my_st.push(i)
    # print(my_st)
    # for _ in range(3):
    #     my_st.pop()
    # print(my_st)

    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать ДЗ", 2)
    print(manager)

    # Результат:
    # 1 — отдохнуть
    # 2 — поесть; сдать ДЗ
    # 4 — сделать уборку; помыть посуду
