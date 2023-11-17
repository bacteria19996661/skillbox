from typing import Callable, Any, Optional


class App:

    def __init__(self):
        """
        Метод-конструктор класса App __init__(self)
        инициализирует объект App и устанавливает атрибут routes в пустой словарь {}.

        Атрибут класса self.routes = {}
        инициализирует пустой словарь routes, где будут храниться маршруты.

        """
        self.routes = {}

    def get(self, path):
        """
        Метод класса get(self, path) принимает аргумент path, который является путем (адресом).
        Используется для получения значения из словаря routes по ключу path.

        return self.routes.get(path):
        Возвращает значение из словаря routes, соответствующее переданному path.
        Если ключ path присутствует в словаре routes, то будет возвращено соответствующее ему значение.
        Если ключ path отсутствует, метод .get() вернет None.
        """
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
    app = App()    # app - экземпляр класса App

    @app.callback(path='//')
    def get_server_response():    # Имитируем ответ от сервера.
        print('Пример функции, которая возвращает ответ сервера.')
        server_response = "ok"
        return server_response

    # Метод get объекта app ищет функцию, связанную с определенным путем '//'.
    # Сохраняем результат (функцию или None) в переменной route.
    route = app.get('//')

    # Проверяем, существует ли значение route в словаре. Если значение существует,
    # это означает, что мы нашли функцию, связанную с путем '//', и условие выполняется.
    # В противном случае, если route равен None, условие не выполняется.
    if route:     # Если route существует (т.е., мы нашли функцию для пути '//'),
        response = route()    # Вызываем функцию, хранящуюся в route.
            # Функция выполняется, и ее результат сохраняется в переменной response.
        print('Ответ:', response)
    else:
        print('Такого пути нет')