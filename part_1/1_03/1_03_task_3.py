# Часть 1. Модуль 3. Задача 3. Следующее и предыдущее числа
#
# Напишите программу, которая получает от пользователя число и выводит на экран
# два ответа — следующее и предыдущее числа.
#
# Что оценивается
# В input содержится корректное приглашение для ввода.
# Вывод соответствует заданию.
# Нет простых print(a), print(a − 1).
# Есть пробелы после запятых в print.

number = int(input('Введите число: '))
print('После числа', number, 'идет число', number + 1)
print('До числа', number, 'идет число', number - 1)
