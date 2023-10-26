#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Часть 2. Модуль 16. Практическая работа. Задача 2. Функция обратного вызова
#
# При работе с сетью и веб-сервисами иногда используется функция callback,
# так называемая функция обратного вызова. Это функция, которая вызывается при срабатывании
# определённого события: переходе на страницу, получении сообщения или окончании обработки процессором.
# В неё можно передать функцию, чтобы она выполнилась после определённого события.
# Это используется, например, в HTTP-серверах в ответ на URL-запросы. Реализуйте такую функцию.
#
# Пример функции:
#
# @callback('//')
# def example():
#     print('Пример функции, которая возвращает ответ сервера')
#     return 'OK'
#
# Основной код:
# route = app.get('//') - тут явно к экземпяру класса App применяется его метод get
# if route:
#     response = route()
#     print('Ответ:', response)
# else:
#     print('Такого пути нет')
# Ожидаемый результат: пример функции, которая возвращает ответ сервера.
# Ответ: OK.
#
# Подсказка: функция callback, в зависимости от условия, может быть вызвана следующим действием или просто так.
#
# Что оценивается в задаче
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы (функции) имеют прописанную документацию.
# Есть аннотация типов для методов (функций) и их аргументов, кроме args и kwargs.
# Если функция или метод ничего не возвращает, то используется None.

from typing import Callable, Any, Optional


class App:
    def __init__(self):
        self.routes = {}

    def get(self, path):
        return self.routes.get(path)

    def callback(self, _func: Optional[Callable] = None, *, path: str = '') -> Callable:
        def callback_decorator(func: Callable) -> Callable:
            self.routes[path] = func  # добаление значения в словарь

            def wrapped_func(*args, **kwargs) -> Any:
                return func(*args, **kwargs)

            return wrapped_func

        if _func is None:
            return callback_decorator
        else:
            return callback_decorator(_func)


if __name__ == '__main__':
    app = App()

    @app.callback(path='//')
    def get_server_response():
        # В реальном приложении здесь будет логика для отправки запроса к серверу и получения ответа.
        # В этом примере мы просто имитируем ответ от сервера.
        print('Пример функции, которая возвращает ответ сервера.')
        server_response = "ok"
        return server_response

    route = app.get('//')
    # Используем метод get объекта app (app - это экземпляр класса App),
    # чтобы найти функцию, связанную с определенным путем '//'.
    # Сохраняем результат (функцию или None) в переменной route.

    # Проверяем, существует ли значение route в словаре. Если значение существует,
    # это означает, что мы нашли функцию, связанную с путем '//', и условие выполняется.
    # В противном случае, если route равен None, условие не выполняется.
    if route:     # Если route существует (т.е., мы нашли функцию для пути '//'),
        response = route()    # Вызываем функцию, хранящуюся в route.
            # Функция выполняется, и ее результат сохраняется в переменной response.
        print('Ответ:', response)
    else:
        print('Такого пути нет')
