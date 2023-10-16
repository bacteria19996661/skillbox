#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Часть 2. Модуль 15. Практическая работа. Задача 1. Работа с файлом 2
# 
# Реализуйте модернизированную версию контекст-менеджера File:
# при попытке открыть несуществующий файл менеджер должен автоматически создавать
# и открывать этот файл в режиме записи;
# на выходе из менеджера должны подавляться все исключения, связанные с файлами.
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений приватных атрибутов используются сеттеры и геттеры
# с соответствующими декораторами.
# Для создания нового класса на основе уже существующего используется наследование.
# Для статических и классовых методов используется декоратор classmethod.
# Сообщения о процессе получения результата осмысленны и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs).
# Если функция/метод ничего не возвращает, то используется None.

import os


class File:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        path = os.path.join(self.file_name)
        abs_path = os.path.abspath(path)
        try:
            self.file = open(abs_path, self.mode, encoding='utf8')
        except FileNotFoundError:
            self.file = open(abs_path, 'w', encoding='utf8')
        return self.file

    def write(self, text):
        return self.file_name.write(text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


if __name__ == '__main__':
    try:
        with File('example', 'r') as file:
            file.write('Всем привет!\n')
    except FileExistsError as exc:
        print(f"Попытка создания файла, который уже существует ({exc}, {type(exc)})")
    except PermissionError as exc:
        print(f"Нет доступа ({exc}, {type(exc)})")
    except FileNotFoundError as exc:
        print(f"Файл не существует ({exc}, {type(exc)})")
    except IsADirectoryError as exc:
        print(f"На чтение ожидался файл, но это оказалась директория ({exc}, {type(exc)})")
    except SyntaxError as exc:
        print(f"Синтаксическая ошибка: ({exc}, {type(exc)})")
    except SystemError as exc:
        print(f"Внутренняя ошибка системы: ({exc}, {type(exc)})")
    except (UnicodeError, UnicodeTranslateError, UnicodeEncodeError, UnicodeDecodeError) as exc:
        print(f"Ошибка, связанная с кодированием или раскодированием unicode в строках ({exc}, {type(exc)})")
    except RuntimeError as exc:
        print(f"Обнаружено исключение: ({exc}, {type(exc)})")
    else:
        print("Программа выполнилась без ошибок.")
