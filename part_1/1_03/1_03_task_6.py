# Часть 1. Модуль 3. Задача 6. Проверяем бухгалтера
#
# Невнимательный бухгалтер Антон складывает числа быстро, но иногда забывает
# о двух последних разрядах. Чтобы помочь Антону, напишите программу, которая бы
# складывала только два последних разряда.
# Реализуйте программу, которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.
#
# Что оценивается
# Результат вычислений корректен.
# В input содержится корректное приглашение для ввода.
# Переменные имеют значащие названия.
# Есть пробелы после запятых и при бинарных операциях.

num1 = int(input('1-е число: '))
num2 = int(input('2-е число: '))
last1 = num1 % 100
last2 = num2 % 100
answer = last1 + last2
print(("1-й остаток: "), last1)
print(("2-й остаток: "), last2)
print(("Ответ: "), answer)
num1 = str(num1)
a = num1[0]
b = num1[1]
c = num1[2]
d = num1[3]
print(f"Строка из цифр: {d + c + b + a}")
print(f"Сумма цифр: {int(a) + int(b) + int(c) + int(d)}")
