#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Часть 2. Модуль 16. Практическая работа. Задача 4. Весь мир — декоратор…
#
# Реализуйте декоратор для декораторов: он должен декорировать другую функцию,
# которая должна быть декоратором, и даёт возможность любому декоратору принимать произвольные аргументы.
#
# Пример использования:
#
# @decorator_with_args_for_any_decorator
# def decorated_decorator(func: Callable, *args, **kwargs):... # отсюда уже сами!
#
# @decorated_decorator(100, 'рублей', 200, 'друзей')
# def decorated_function(text: str, num: int) -> None:
#     print("Привет", text, num)
#
# decorated_function("Юзер", 101)
#
# Результат:
# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs).
# Если функция/метод ничего не возвращают, то используется None.

import functools
from typing import Callable, Any


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """
    Декоратор для декораторов.
    Декорирует другую функцию, которая должна быть декоратором,
    и даёт возможность любому декоратору принимать произвольные аргументы.

    :param decorator: принимает функцию-декоратор
    :return decorator_wrapper: возвращается результат выполнения внутренней функции (с аргументами)
    принимаемого декоратора, а также результат выполнения самого принимаемого декоратора (с аргументами).
    """
    def decorator_wrapper(*args, **kwargs) -> Callable:
        """
        Декоратор, который принимает аргументы для декорируемого декоратора.

        :param args, kwargs: аргументы для декорируемого декоратора.
        :return decorated_decorator: возвращается сам декорируемый декоратор
        """
        def decorated_decorator(func: Callable) -> Callable:
            """
            Декорируемый декоратор.

            :param func: принимается функция
            :return decorator(wrapped_func, *args, **kwargs): Возвращается принимаемый декоратор
            (с результатом выполнения функции и аргументами декоратора).
            """
            print(f"Переданные в декоратор аргументы: {args} {kwargs}")

            @functools.wraps(func)
            def wrapped_func(*func_args, **func_kwargs) -> Any:
                """
                Внутренняя функция обертки, куда передаются аргументы func.

                :param func_args, func_kwargs: аргументы функции func
                :return func(*func_args, **func_kwargs): Возвращается внутренняя функция принимаемого декоратора.
                """
                return func(*func_args, **func_kwargs)
            return decorator(wrapped_func, *args, **kwargs)

        return decorated_decorator

    return decorator_wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:

    @functools.wraps(func)
    def wrapped_func(*func_args, **func_kwargs) -> Any:   # внутренняя функция обертки, сюда передаются аргументы func
        print(f'Декоратор передает и возвращает '
              f'внутреннюю функцию с аргументами {func_args} {func_kwargs}')
        return func(*func_args, **func_kwargs)

    return wrapped_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)



# РЕШЕНИЕ SKILLBOX:
#
# from typing import Callable
# import functools
#
# # Реализовать декоратор для декораторов
#
# ----------- СЛЕДУЮЩИЙ ЭТАП --------------------
# def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable):
#     """ Декоратор. Дает возможность другому декоратору принимать произвольные аргументы.
#         Пишем далее как в уроке про декораторы с аргументами. """
#     def decorator_maker(*args, **kwargs) -> Callable:
#         # Далее создаем декоратор, который принимает только функцию, но сохраняет все аргументы,
#                 переданные своему создателю)
#         def decorator_wrapper(func: Callable) -> Callable:
#             # ниже возвращаем то, что вернет нам изначаьный декоратор,
#                 # который, в свою очередь, является просто функцией,
#                     # возвращая другую функцию
#             return decorator_to_enhance(func, *args, **kwargs)
#         return decorator_wrapper
#     return decorator_maker
#
#
# ----- ПЕРВЫЙ ЭТАП ----------------
# @decorator_with_args_for any_decorator    # Следующим этапом надо задекорировать этот декоратор,
#                         # написав для него декоратор, принимающий произвоьные аргументы для декораторов
# def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
#    " Декоратор шаблон "
#     @functools.wraps(func)
#     def wrapper(*func_args, **func_kwargs) -> Callable:
#         print("Переданные в декоратор арги и кварки", dec_args, dec_kwargs)
#         return func(*func_args, **func_kwargs)
#     return wrapper
#
#
# ---- ИСХОДНЫЕ ДАННЫЕ ------------------
# @decorated_decorator(100, 'рубей', 200, 'друзей')
# def decorated_function(text: str, num: int) -> None:
#     " Пример декорируемой функции "
#     print("Привет", text, num)
#
#
# decorated_function("Юзер", 101)
