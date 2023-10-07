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

from typing import Any, Optional    # два специаьных класса для аннотации типов


class Node:    # УЗЕЛ
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value    # значение
        self.next = next    # ссылка на следующий узел

    def __str__(self) -> str:
        return 'Node [{value}]'.format(value=str(self.value))

class LinkedList:    # СПИСОК узлов
    def __init__(self) -> None:
        self.head: Optional[Node] = None    # указатель на самый первый головной элемент (узел списка или None)
        self.length = 0    # инициализируем счетчик длины для метода удаления элемента

    def __str__(self) -> str:    # переопределим вывод
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList []'

    def append(self, elem: Any) -> None:    # Добавение элемента (Any - любого) в конец списка
        new_node = Node(elem)    # создаем узел, который будет содержать передаваемые методом append данные
        if self.head is None:    # если список пустой,
            self.head = new_node    # то атрибут head будет указывать на этот же узел
            return    # выходим

        # если в списке уже есть узлы, то нужно пройтись по всем узлам до последненго и связать его с новым
        last = self.head    # поместили указатель на первый элемент в переменную last
        while last.next:    # если атрибут next не равен None, то у него есть следующий сосед
            last = last.next    # его и берем
        last.next = new_node    # последним узлом сделаем соседа
        self.length += 1    # увеличиваем счетчик длины для метода удаления элемента

    def get(self, index) -> None:
        cur_node = self.head
        cur_index = 0
        # if self.length == 0 or self.length <= index:
        #     raise IndexError

        if cur_node is not None:  # Если текущий указатель не пустой, то
            if index == 0:  # Если ищем первый элемент, то
                print(self.head)
                return self.head

        while cur_node is not None:    # то проходим циклом по всем узлам,
            if cur_index == index:    # и сравниваем текущий индекс с переданным
                break    # если нашли его, выходим
            # внутри цикла идем по списку,
            prev = cur_node    # запоминаем предыдущий узел
            cur_node = cur_node.next    # и переходим к следующему узлу, до тех пор пока не выполнится условие цикла
            cur_index += 1
        # когда нашли узел с нужным значением,
        print(cur_node)
        return cur_node

    def remove(self, index) -> None:
        cur_node = self.head    # создадим переменную для указателя, чтобы случайно не поменять первый элемент head
        cur_index = 0    # создадим переменную для текущего индекса
        if self.length == 0 or self.length <= index:    # Проверим, не выходит ли индекс за границы списка
            raise IndexError    # для этого при добавлении элемента нужно считать длину (инициализируем её в списке)

        if cur_node is not None:  # Если текущий указатель не пустой, то
            if index == 0:    # Если удаляем первый элемент, то
                self.head = cur_node.next    # достаточно заменить его ссылку на ссылку следующего элемента (узла)?
                self.length -= 1    # уменьшить длину
                return    # и выйти из метода
        # если удаляется не первый элемент,
        while cur_node is not None:    # то проходим циклом по всем узлам,
            if cur_index == index:    # и сравниваем текущий индекс с переданным
                break    # если нашли его, выходим
            # внутри цикла идем по списку,
            prev = cur_node    # запоминаем предыдущий узел
            cur_node = cur_node.next    # и переходим к следующему узлу, до тех пор пока не выполнится условие цикла
            cur_index += 1
        # когда нашли узел с нужным значением,
        print(cur_node)
        prev.next = cur_node.next    # заменяем ссылку на следующий узел
        self.length -= 1    # и уменьшаем длину
        # Это полноценное удаление, т.к. в памяти узел не остается, ведь на него никто не ссылается,
            # сборщик мусора автоматически удалит его из памяти



if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)    # тут запустить дебаг
    my_list.append(30)
    print('Текущий список:')
    print(my_list)
    print('Получение элемента:')
    my_list.get(2)
    print('Удаление элемента:')
    my_list.remove(1)
    print('Новый список:')
    print(my_list)