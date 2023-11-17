from typing import Callable, Any, Optional


class App:

    def __init__(self):
        """
        �����-����������� ������ App __init__(self)
        �������������� ������ App � ������������� ������� routes � ������ ������� {}.

        ������� ������ self.routes = {}
        �������������� ������ ������� routes, ��� ����� ��������� ��������.

        """
        self.routes = {}

    def get(self, path):
        """
        ����� ������ get(self, path) ��������� �������� path, ������� �������� ����� (�������).
        ������������ ��� ��������� �������� �� ������� routes �� ����� path.

        return self.routes.get(path):
        ���������� �������� �� ������� routes, ��������������� ����������� path.
        ���� ���� path ������������ � ������� routes, �� ����� ���������� ��������������� ��� ��������.
        ���� ���� path �����������, ����� .get() ������ None.
        """
        return self.routes.get(path)

    def callback(self, _func: Optional[Callable] = None, *, path: str = '') -> Callable:
        def callback_decorator(func: Callable) -> Callable:
            self.routes[path] = func  # ��������� �������� � �������

            def wrapped_func(*args, **kwargs) -> Any:
                return func(*args, **kwargs)

            return wrapped_func

        if _func is None:
            return callback_decorator
        else:
            return callback_decorator(_func)


if __name__ == '__main__':
    app = App()    # app - ��������� ������ App

    @app.callback(path='//')
    def get_server_response():    # ��������� ����� �� �������.
        print('������ �������, ������� ���������� ����� �������.')
        server_response = "ok"
        return server_response

    # ����� get ������� app ���� �������, ��������� � ������������ ����� '//'.
    # ��������� ��������� (������� ��� None) � ���������� route.
    route = app.get('//')

    # ���������, ���������� �� �������� route � �������. ���� �������� ����������,
    # ��� ��������, ��� �� ����� �������, ��������� � ����� '//', � ������� �����������.
    # � ��������� ������, ���� route ����� None, ������� �� �����������.
    if route:     # ���� route ���������� (�.�., �� ����� ������� ��� ���� '//'),
        response = route()    # �������� �������, ���������� � route.
            # ������� �����������, � �� ��������� ����������� � ���������� response.
        print('�����:', response)
    else:
        print('������ ���� ���')