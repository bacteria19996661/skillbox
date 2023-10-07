#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Часть 2. Модуль 14. Практическая работа. Задача 2. Замедление кода
#
# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.
#
# Что оценивается
# Результат вычислений корректен.
# Сообщения о процессе получения результата осмыслены и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs).
# Если функция/метод ничего не возвращает, то используется None.
# Во всех декораторах используется functools.wraps().

import time
from typing import Callable, Any    # Для аннотации объектов
import functools    # модуль с инструментами для избежания проблем декораторов
# при работе с магическими методами оборачиваемых функций (получение информации о функции)


def timer(func: Callable) -> Callable:
    """ Декоратор. Выводит время работы функции после паузы 3 сек. """

    @functools.wraps(func)
    # декоратор wraps, которому передаем оборачиваемую функцию для избежания проблем декораторов
    def wrapped_func(*args, **kwargs) -> Any:
        print('Ждем 3 сек.')
        time.sleep(3)
        print('Выполняем код:')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = round(end - start, 4)
        print('Функция работала {} секунд(ы).'.format(run_time))

        return result

    return wrapped_func

@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])

    return result

my_cubes_sum = cubes_sum(200)
print(my_cubes_sum)
