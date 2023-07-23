# Модуль 5. Задача 3. Поступление
#
# Напишите программу, которая получает на вход место студента в списке и его балл,
# а затем выводит соответствующие сообщения о поступлении и получении стипендии.
#
# Пример 1:
# Введите место в списке поступающих: 3
# Введите количество баллов за экзамены: 295
# Поздравляем, вы поступили!
# Бонусом вам будет начисляться стипендия.
#
# Пример 2:
# Введите место в списке поступающих: 3
# Введите количество баллов за экзамены: 270
# Поздравляем, вы поступили!
# Но вам не хватило баллов для стипендии.
#
# Пример 3:
# Введите место в списке поступающих: 11
# К сожалению, вы не поступили.
#
# Что оценивается
# результат вывода корректен и соответствует примеру;
# input содержит корректное приглашение для ввода;
# переменные имеют значащие имена, а не только a, b, c, d (видео 2.3);
# правильное употребление пробелов после запятых при бинарных и логических операциях;
# правильно оформлены блоки if-elif-else, отступы одинаковы во всех блоках одного уровня.


num = int(input('Введите место студента в списке: '))
if (num <= 10):
    print('Студент поступил')
    point = int(input('Введите кол-во его баллов: '))
    if point >= 290:
        print('Студент будет получать стипендию')
    else:
        print('Студент не будет получать стипендию')
else:
    print('Студент не поступил.')