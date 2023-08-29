# Часть 1. Модуль 5. Задача 7. Почта
#
# Почтовое отделение открывается в 08:00 и закрывается в 22:00.
# С 14:00 до 15:00 все сотрудники уходят на обед, а в 10:00 и 18:00
# приезжают машины с посылками, и все сотрудники на два часа заняты их разгрузкой.
# Во время обеда и разгрузки машин  посылки никто не выдаёт.
#
# Напишите программу, которая получает на вход время в часах —
# число от 0 до 23 — и пишет, можно ли в этот час получить посылку.
# спользуйте только один условный оператор if-else, без elif и прочих.
# Решите задание двумя способами:
#
# При выполнении условия выводится сообщение: «Можно получить посылку».
# При выполнении условия выводится сообщение: «Посылку получить нельзя».
# Советы и рекомендации
# Обратите внимание на количество условий и постарайтесь сократить их.
# Не используйте перечисление конкретных часов вида a == 1 and a == 2...
#
# Что оценивается
# результат вычислений корректен;
# input содержит корректное приглашение для ввода;
# переменные имеют значащие имена, а не только a, b, c, d (видео 2.3);
# правильное употребление пробелов после запятых и при бинарных операциях.

time = int(input('Введите время, ч: '))

def task_5_7():
    if (8 >= time < 10) or (12 >= time < 14) or (15 >= time < 18) or (20 >= time < 22):
        print('Можно получить посылку.')
    else:
        print('Посылку получить нельзя.')

def task_5_7_2():
    if not (8 <= time < 22) or (10 <= time <= 12) or (14 <= time <= 15) or (18 <= time <= 20):
       print('Посылку получить нельзя.')
    else:
       print('Можно получить посылку.')

task_5_7()
task_5_7_2()
