#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 15. Практическая работа. Задача 3. Дата
#
# Реализуйте класс Date, который должен:
# проверять числа даты на корректность;
# конвертировать строку даты в объект класса Date, состоящий из
# соответствующих числовых значений дня, месяца и года.
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.
#
# При тестировании программы объект класса Date должен инициализироваться
# исключительно через метод конвертации, например:
#
# date = Date.from_string('10-12-2077')
# Неверный вариант: date = Date(10, 12, 2077)
#
# Пример основного кода:
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-12-2077'))
# print(Date.is_date_valid('40-12-2077'))
# Результат:
# День: 10    Месяц: 12    Год: 2077
# True
# False
#
# Что оценивается
# Результат вычислений корректен.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений приватных атрибутов используются сеттеры и геттеры с
# соответствующими декораторами.
# Для создания нового класса на основе уже существующего используется наследование.
# Для статических и классовых методов используется декоратор classmethod.
# Формат вывода соответствует примеру.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs).
# Если функция/метод ничего не возвращает, то используется None.

# Решение Skillbox

class Date:
    def __init__(self, day: int = 0, month: int = 0, year: int = 0,) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return 'День: {day}\tМесяц: {month}\tГод: {year}'.format(
            day=self.day, month=self.month, year=self.year
        )

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        """
        Метод проверяет числа даты на корректность
        :param date (str):
        :return: True, если строка корректна, иначе False
        """
        # date_list = date.split('-')
        # day, month, year = int(date_list[0]), int(date_list[1]), int(date_list[2])
        day, month, year = map(int, date.split('-'))

        return 0 < day <= 31 and 0 < month <= 12 and 0 <= year <= 9999

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        """
        Метод конвертирует строку даты в объект класса Date,
        состоящий из соответствующих числовых значений дня, месяца и года.
        :param date:
        :return: Date - объект
        """
        day, month, year = map(int, date.split('-'))
        obj = cls(day, month, year)
        return obj


if __name__ == '__main__':
    my_date = Date.from_string('10-12-2077')
    print('Тест:', my_date)
    print(Date.is_date_valid('10-12-2077'))
    print(Date.is_date_valid('40-12-2077'))





# МОЕ РЕШЕНИЕ
# class Date:
#     def __init__(self) -> None:
#         self.ds = ''
#         self.day = 0
#         self.month = 0
#         self.year = 0
#
#     def __str__(self):
#         return 'День: {day}\tМесяц: {month}\tГод: {year}'.format(
#             day=self.day, month=self.month, year=self.year
#         )
#
#     def is_date_valid(self, ds: str) -> bool:
#         """
#         Метод проверяет числа даты на корректность
#         :param date_str:
#         :return: True, если строка корректна, иначе False
#         """
#         try:
#             for _ in ds:
#                 if (1 <= int(ds[:2]) <= 31 and 1 <= int(ds[3:5]) <= 12 and ds[2] == ds[5] == '-'
#                         and 0 < int(ds[6:]) <= 9999):
#                     return True
#                 return False
#         except (ValueError, Exception) as err:
#             print(err, type(err))
#
#     def from_string(self, ds: str) -> tuple:
#         """
#         Метод конвертирует строку даты в объект класса Date,
#         состоящий из соответствующих числовых значений дня, месяца и года.
#         :param ds:
#         :return:
#         """
#
#         ds_list = ds.split('-')
#         self.day, self.month, self.year = ds_list[0], ds_list[1], ds_list[2]
#         return self.day, self.month, self.year
#
#
#
# if __name__ == '__main__':
#     usr_date = ['10-12-2077', '40-12-2077', 'ffhgfg', input('Введите дату в формате dd-mm-yyyy: ')]
#     Date = Date()
#     for i_date in usr_date:
#         print('Тест:', i_date)
#         result = Date.is_date_valid(i_date)
#         print(result)
#         if result:
#             Date.from_string(i_date)
#             print(Date)
#         print('------')
