#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from datetime import datetime

def log_methods(date_format: str):
    def decorator(cls):
        class DecoratedClass(cls):
            def __getattribute__(self, attr_name):
                attr = super().__getattribute__(attr_name)
                if callable(attr) and not attr_name.startswith("__"):
                    def wrapped_method(*args, **kwargs):
                        start_time = time.time()
                        now = datetime.now()
                        formatted_date_time = now.strftime(date_format)
                        print(f"Запускается '{attr_name}'. Дата и время запуска: {formatted_date_time}.")

                        result = attr(*args, **kwargs)

                        end_time = time.time()
                        execution_time = end_time - start_time
                        print(f"Завершение '{attr_name}', время работы = {execution_time:.3f} s.")

                        return result

                    return wrapped_method
                return attr

        return DecoratedClass

    return decorator

@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

@log_methods("%b %d %Y — %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника")

    def test_sum_2(self):
        print("Тут метод test_sum_2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
