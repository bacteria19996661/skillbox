#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Часть 2. Модуль 16. Практическая работа. Задача 1. Права доступа
#
# Напишите декоратор check_permission, который проверяет,
# есть ли у пользователя доступ к вызываемой функции,
# и если нет, то выдаёт исключение PermissionError.
#
# Пример кода:
#
# user_permissions = ['admin']
#
# @check_permission('admin')
# def delete_site():
#     print('Удаляем сайт')
#
# @check_permission('user_1')
# def add_comment():
#     print('Добавляем комментарий')
#
# delete_site()
# add_comment()
#
# Результат:
# Удаляем сайт
# PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию add_comment
#
# Что оценивается в задаче
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов, кроме args и kwargs.
# Если функция/метод ничего не возвращает, то используется None.


# Простой вариант:
# def check_permission(usr: str):
#     def permission_decorator(func):
#         @functools.wraps(func)
#         def wrapped_func(*args, **kwargs):
#             if usr in user_permissions:
#                 return func(*args, **kwargs)
#             else:
#                 raise PermissionError('У пользователя недостаточно прав, чтобы выполнить функцию', func.__name__)
#
#         return wrapped_func
#
#     return permission_decorator


from typing import Callable, Any, Optional


def check_permission(_func: Optional[Callable] = None, *,
                     usr_permissions: list, req_permission: str = '') -> Callable:
    def permission_decorator(func: Callable) -> Callable:
        def wrapped_func(*args, **kwargs) -> Any:
            if req_permission in usr_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError('У пользователя недостаточно прав, чтобы выполнить', func)

        return wrapped_func

    if _func is None:
        return permission_decorator
    else:
        return permission_decorator(_func)


if __name__ == '__main__':
    user_permissions = ['admin']

    @check_permission(usr_permissions=user_permissions, req_permission='admin')
    def delete_site():
        print('Удаляем сайт')

    @check_permission(usr_permissions=user_permissions, req_permission='user_1')
    def add_comment():
        print('Добавляем комментарий')

    delete_site()  # Выполнится, т.к. 'admin' is in user_permissions
    add_comment()  # raise PermissionError, т.к. 'user_1' is not in user_permissions
