# Модуль 7. Задача 4. Успеваемость в классе
#
# В классе N человек. Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
# Напишите программу, которая получает список оценок — N чисел — и выводит на экран
# сообщение о том, кого сегодня больше: отличников, хорошистов или троечников.
#
# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.
#
# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# в выводе присутствует сообщение о том, кого больше;
# для решения используется цикл for, а не встроенные функции или рекурсия;
# переменные имеют значащие имена, не только a, b, c, d.

string_mark = input('Введите оценки учеников подряд без разделителей: ')

# Решение 1:
def task_7_4_1():

    list_mark = []
    flag = False
    
    for i in string_mark:
        i = int(i)
        list_mark.append(i)
        if i != 3 and i != 4 and i != 5:
            flag = True
    if flag is True:
        print('В классе не должно быть учеников с отметками, отличными от 3, 4 или 5. Поэтому их мы не засчитываем.')
   
    normal = list_mark.count(3)
    good = list_mark.count(4)
    excellent = list_mark.count(5)
    
    if normal > good and normal > excellent:
        print('Сегодня больше всего троешников, их', normal)
    elif good > normal and good > excellent:
        print('Сегодня больше всего хорошистов: их', good)
    elif excellent > normal and excellent > good:
        print('Сегодня больше всего отличников: их', excellent)
    elif normal == good and good == excellent:
        print('Сегодня всех по', normal)
    else:
        if normal == good:
            print('Троешников и хорошистов по', normal)
        elif normal == excellent:
            print('Троешников и отличников по', normal)
        else:
            print('Хорошистов и отличников по', good)
   
    print('Подробно:')
    print('Сегодня получили оценки n учеников.')
    list_mark.sort()
    print(list_mark)
    print('Троешников: ', list_mark.count(3))
    print('Хорошистов: ', list_mark.count(4))
    print('Отличников: ', list_mark.count(5))

# Решение 2:

def task_7_4_2():
    
    n = len(string_mark)
    list_mark = []
    flag = False
    
    for i in range (0,n):
        list_mark.insert(i, string_mark[i])
        if int(string_mark[i]) != 3 and int(string_mark[i]) != 4 and int(string_mark[i]) != 5:
            flag = True
    if flag is True:
        print('В классе не должно быть учеников с отметками, отличными от 3, 4 или 5.')
        
    normal = list_mark.count('3')
    good = list_mark.count('4')
    excellent = list_mark.count('5')
    
    if normal > good and normal > excellent:
        print('Сегодня больше всего троешников, их', normal)
    elif good > normal and good > excellent:
        print('Сегодня больше всего хорошистов: их', good)
    elif excellent > normal and excellent > good:
        print('Сегодня больше всего отличников: их', excellent)
    elif normal == good and good == excellent:
        print('Сегодня всех по', normal)
    else:
        if normal == good:
            print('Троешников и хорошистов по', normal)
        elif normal == excellent:
            print('Троешников и отличников по', normal)
        else:
            print('Хорошистов и отличников по', good)
            
    print('Подробно:')
    print('Сегодня получили оценки', n,'учеников.')
    list_mark.sort()
    print(list_mark)
    print('Троешников: ', list_mark.count('3'))
    print('Хорошистов: ', list_mark.count('4'))
    print('Отличников: ', list_mark.count('5'))

task_7_4_1()
# task_7_4_2()