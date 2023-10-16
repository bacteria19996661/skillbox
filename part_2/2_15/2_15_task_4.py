#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 15. Практическая работа. Задача 4. Кэширование запросов
#
# Вы разрабатываете программу для кэширования запросов к внешнему API.
# Часто повторяющиеся запросы занимают много времени, поэтому
# вы решаете создать класс LRU Cache (Least Recently Used Cache),
# который будет хранить ограниченное количество запросов и
# автоматически удалять самые старые при достижении лимита.
# Это позволит значительно ускорить повторяющиеся запросы,
# так как данные будут браться из кэша, а не отправляться повторно.
#
# Задача
# Создайте класс LRU Cache, который хранит ограниченное количество объектов и,
# при превышении лимита, удаляет самые давние (самые старые) использованные элементы.
# Реализуйте методы добавления и извлечения элементов с использованием декораторов property и setter.
# @property
# def cache(self): # этот метод должен возвращать самый старый элемент
# ...
# @cache.setter
# def cache(self, new_elem): # этот метод должен добавлять новый элемент
# ...
# Советы
# Не забывайте обновлять порядок использованных элементов.
# В итоге должны удаляться давно использованные элементы, а не давно добавленные,
# так как давно добавленный элемент может быть популярен, и его удаление не поможет ускорить новые запросы.


from typing import Any
from collections import OrderedDict


class LRUCache:
    """
    Класс реализует функциональность:
        Класс LRU Cache хранит ограниченное количество объектов и,
        при превышении лимита, удаляет элементы, которые давно не использовались.

    Свойства:
        cache(self): возвращает самый старый элемент
        cache(self, key_value_tuple): принимает кортеж и разбивает его на key:value.

    Методы:
        add_to_cache(self, key: Any, value: Any) setter -> Any:
            Удаляет наименее используемый элемент.
            Сохраняет в кеш key: value и частотный кеш key: usage_count
        get(self, key: Any) -> Any: Возвращает значение по ключу
        print_cache(self) -> None: Выводит актуальные значения кеш

    Notes:
        LRU Cache (Least Recently Used Cache), который будет хранить ограниченное количество запросов
        и автоматически удалять самые старые при достижении лимита.
        Это позволит значительно ускорить повторяющиеся запросы, так как данные будут браться из кэша,
        а не отправляться повторно.
    Cловарь usage_count используется, чтобы отслеживать частоту использования каждого элемента.
    При превышении лимита кеша удаляется наименее используемый элемент.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = OrderedDict()  # Use an OrderedDict to maintain the order of elements
        self.usage_count = OrderedDict()  # Use another OrderedDict to store usage count of elements

    @property
    def cache(self):    # возвращает самый старый элемент
        least_used_key = min(self.usage_count, key=self.usage_count.get, default=None)
        if least_used_key is None:
            return None

        self.usage_count.pop(least_used_key)
        return self.cache_dict.pop(least_used_key)

    @cache.setter
    def cache(self, key_value_tuple):    # Принимает кортеж и разбивает его на key:value.
        key, value = key_value_tuple
        self.add_to_cache(key, value)

    def add_to_cache(self, key: Any, value: Any) -> Any:
        """
        Метод добавления нового элемента.

        Если key уже есть в словаре, перемещает существующий элемент в конец словаря cache_dict
        и будет считаться недавно использованным).
        Встроенный в упорядоченные словари метод .move_to_end() позволяет переместить
        существующий элемент в конец или в начало словаря.
        Элемент перемещается в правый конец, если аргумент last=True (по умолчанию).

        Иначе, если длина cache_dict больше заданного значения capacity,
        то ищем редко используемый элемент и удаляем его.

        Для нахождения используется метод min. Он принимает функцию key=self.usage_count.get,
        что означает, что минимум будет определен на основе значений, возвращаемых методом get
        для каждого ключа из usage_count.
        После того как был найден наименее используемый ключ, соответствующая ему запись удаляется
        как из cache_dict, так и из usage_count.

        Затем новый элемент добавляется в cache_dict с ключом key и соответствующим значением value.
        Также обновляется счетчик использования для данного ключа в usage_count, увеличивая его на 1.

        :param key: ключ, добавляемый в кеш
        :param value: значение ключа
        """
        if key in self.cache_dict:
            # Move the accessed element to the end (most recently used)
            self.cache_dict.move_to_end(key)
        else:
            # Check if the cache is full
            if len(self.cache_dict) >= self.capacity:
                # Find the least used element and remove it
                if self.cache is None:
                    return  # Cache is empty, nothing to remove

        self.cache_dict[key] = value  # Add the new element to the cache
        self.usage_count[key] = self.usage_count.get(key, 0) + 1  # Update the usage count

    def get(self, key: Any) -> Any:
        """
        Метод принимает аргумент key и возвращает его значение, увеличивая счетчик использования.

        Если key присутствует в cache_dict, то
        элемент с данным ключом перемещается в конец с помощью метода move_to_end.
        Обновляется счетчик использования для данного ключа в usage_count, увеличивая его на 1.
        Возвращается значение, соответствующее ключу key из cache_dict.
        Если key не найден в cache_dict, то возвращается None.
        :param key:
        :return: cache_dict[key] или None
        """
        if key in self.cache_dict:
            # Move the accessed element to the end (most recently used)
            self.cache_dict.move_to_end(key)
            # Update the usage count for the accessed element
            self.usage_count[key] = self.usage_count.get(key, 0) + 1
            return self.cache_dict[key]
        else:
            return None

    def print_cache(self) -> None:
        """ Вывод словаря. """
        for key, value in self.cache_dict.items():
            print(f'{key} : {value}')


if __name__ == '__main__':
    cache = LRUCache(3)

    # Use the add_to_cache method to set a new key-value pair
    cache.cache = "key1", "value1"
    cache.cache = "key2", "value2"
    cache.cache = "key3", "value3"

    print("LRU Cache:")
    cache.print_cache()  # Output: key1 : value1, key2 : value2, key3 : value3

    print(cache.get("key2"))  # Output: value2
    print(cache.get("key1"))  # Output: value1
    print(cache.get("key2"))  # Output: value2
    print(cache.get("key2"))  # Output: value2
    print(cache.get("key3"))  # Output: value3
    print(cache.get("key1"))  # Output: value1
    print(cache.get("key2"))  # Output: value2
    print(cache.get("key3"))  # Output: value3
    print(cache.get("key2"))  # Output: value2
    print(cache.get("key2"))  # Output: value2
    print(cache.get("key1"))  # Output: value1
    print(cache.get("key2"))  # Output: value2
    print(cache.get("key3"))  # Output: value3

    # Use the add_to_cache method to set new key-value pairs
    cache.cache = "key4", "value4"
    cache.cache = "key5", "value5"

    print("LRU Cache:")
    cache.print_cache()
