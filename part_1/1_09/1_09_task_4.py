# Модуль 9. Задание 4. Марсоход-2
#
# К роботу Валли отправили «коллегу» Билли. Это его первая высадка на Марс,
# поэтому его тестируют в прямоугольном помещении размером 15 × 20 м.
# Марсоход высаживается в центре комнаты (в точке 8, 10), затем управление им
# передаётся оператору, то есть пользователю вашей программы.
#
# Программа спрашивает, в какую сторону оператор хочет направить робота:
# север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D).
# Оператор делает выбор, марсоход перемещается в эту сторону на один метр,
# а программа сообщает новую позицию робота. Если марсоход упёрся в стену,
# он не должен пытаться переместиться в сторону стены — в этом случае его позиция не меняется.
#
# Создайте программу для управления роботом Билли.
#
# Пример:
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
#
# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# формат вывода соответствует примеру;
# марсоход не двигается, если достигает границы участка;
# программа игнорирует регистр вводимых команд;
# переменные имеют значащие имена, не только a, b, c, d (видео 2.3).
#
# Рекомендации по выполнению
# Обращайте внимание на границы.
# Попробуйте изменять положение марсохода только после проверки координат.
# Ввод команд происходит только в верхнем регистре, учитывать нижний не нужно.
# Старайтесь максимально уменьшать количество дублирований кода.
# Если действие выполняется независимо от условий - его не стоит дублировать в каждом условии.

dim_X, dim_Y = 15, 20
X, Y = 8, 10

print(f"Управление марсоходом:\n Cевер - W\n Юг - S\n Запад - A\n Восток - D\n \n")

while (X != 1) and (Y != 1) and (X != dim_X) and (Y != dim_Y):
    team = input(f"Марсоход находится на позиции ({X},{Y}) введите команду: ")
    if team == 'W' or team == 'w':
        Y += 1
    elif team == 'S' or team == 's':
        Y -= 1
    elif team == 'A' or team == 'a':
        X += 1
    elif team == 'D' or team == 'd':
        X -= 1
    else:
        print(f"Команда не распознана! Введите другую.")

print('Вы врезались в стену! Тест завершен.\n')