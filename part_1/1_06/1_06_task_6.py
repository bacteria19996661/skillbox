# Модуль 6. Задача 6. Вклады
#
# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.
# Определите, через сколько лет вклад составит не менее Y рублей.
#
# Напишите программу, которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.
#
# Что оценивается:
# Результат вычислений корректен.
# Input содержит корректное приглашение для ввода.
# Переменные имеют значащие имена, не только a, b, c, d (видео 2.3).
# Правильное употребление пробелов после запятых и при бинарных операциях.


contribution_start = int(input('Введите сумму вклада: '))
contribution_final = int(input('Введите желаемую сумму: '))

if contribution_final < contribution_start:
    print('Вам нужно снять деньги в размере', contribution_start - contribution_final)
else:
    percent = int(input('Введите годовой процент по вкладу от 0 до 100: '))
    count = 1
    while contribution_start <= contribution_final:
        contribution_start = contribution_start + contribution_start * percent / 100
        contribution_start = contribution_start // 1
        print('Через', count, 'лет у вас будет: ', contribution_start)
        count += 1
    print('Нужная сумма в размере', contribution_final, 'руб. наберется через', count - 1, 'лет.')
