# Часть 1. Модуль 9.

def task_9_1():
    print('\nЗадача 9-1 - «Я стал новым пиратом!» \n')

    need_word = 'Карамба'
    count = 0

    for yours_word in range(10):
        yours_word = input('Кричите: ')
        if yours_word == need_word:
            count += 1

    print(f"\nКол-во верных ответов: {count} \n")


def task_9_2():
    print('\nЗадача 9-2 - Кривой мессенджер (определяет порядковый номер звёздочки в строке).\n')

    need_symbol = '*'
    word = input('Введите слово: ')

    count = 1

    for symbol in word:
        if symbol != need_symbol:
            count += 1
        else:
            print(f"\nСимвол «*» стоит на позиции {count} \n")
            break


def task_9_3():
    print('\nЗадача 9-3 - Театр (получает на вход количество рядов, сидений и свободных метров между рядами, а затем выводит примерный макет театра на экран).\n')

    rows = int(input('\nВведите кол-во рядов: '))
    seats = int(input('Введите кол-во сидений: '))
    distance = int(input('Введите расстояние между рядами в метрах: '))
    print()

    for i in range(rows):
        print('=' * seats, '*' * distance, '=' * seats)


def task_9_4():
    print('\nЗадача 9-4 - Марсоход-2\n')

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


def task_9_5():
    print('\nЗадача 9-5 - Великий и могучий (получает на вход текст и находит длину самого длинного слова).\n')

    text = (input('\nВведите текст:\n\n'))

    sub_text = text.split(' ')
    length_sub_text = []

    for item in sub_text:
        length_sub_text.append(len(item))

    print(f"\nСамое длинное слово в строке - {sub_text[int(length_sub_text.index(max(length_sub_text)))]}\n")


def task_9_6():
    print('\nЗадача 9-6 - Коровы (пользователь вводит строку из десяти символов a и b. Определить, сколько будет молока за день?)\n')

    distribution = "abaabaaaba"
    total_milks = 0

    for number, letter in enumerate(distribution):
        if letter == "b":
            total_milks += (number + 1) * 2
    print(f"\nВсего молока будет за день: {total_milks}\n")


def task_9_6_2():
    print('Задача 9-6 - Коровы (альтернативное решение через список).\n')

    distribution = input('Распределите коров по 10 стойлам (a — свободное, b — занятое):\n')

    if len(distribution) != 10:
        print(f"У вас 10 мест! Вы заполнили {len(distribution)} мест.")
    else:

        milks = []

        for milk in range(2, 21, 2):
            milks.append(milk)

        count = 0
        total_milks = 0

        for check in distribution:
            if check == 'b':
                total_milks += milks[count]
            count += 1

        print(f"\nВсего молока будет за день: {total_milks}\n")


def task_9_7():
    print('Задача 9-7 - Метод бутерброда \n')
    input_word = 'В?иаккттоур ияяа,н тгадвео рмкодяо п'
    corrective = 0

    if len(input_word) % 2 == 0:
        corrective = 1

    print(f"Зашифрованное слово: {input_word[0:len(input_word):2] + input_word[len(input_word) - 2 + corrective:0:-2]}")


def task_9_8():
    print('Задача 9-8 - Метод бутерброда - обратная задача\n')
    input_phrase = 'Как видно, в литеральной форме кортеж python 3 записывается в виде последовательности ' \
                   'элементов в круглых скобках, в то время как для списков характерны квадратные. Некоторые ' \
                   'особенности кортежей: они упорядочены по позициям; tuple могут хранить и содержать внутри себя ' \
                   'объекты любых типов (и даже составных); доступ к элементам происходит по смещению, а не по ключу; ' \
                   'в рамках этой структуры данных определены все операции, основанные на применении смещения ' \
                   '(индексирование, срез); кортежи поддерживают неограниченное количество уровней вложенности; ' \
                   'кортежи хранят указатели на другие объекты, а значит их можно представлять, как массивы ссылок; ' \
                   'они позволяют очень просто менять местами значения двух переменных. Зачем использовать кортеж ' \
                   'вместо списка? Тем, кто уже успел познакомиться со списками в Python, может показаться не ' \
                   'очевидным смысл использования кортежей. Ведь фактически, списки могут делать всё то же самое ' \
                   'и даже больше. Это вполне естественный вопрос, но, разумеется, у создателей языка найдётся на ' \
                   'него ответ: Неизменяемость — именно это свойство кортежей, порой, может выгодно отличать их ' \
                   'от списков. Скорость — кортежи быстрее работают. По причине неизменяемости кортежи хранятся в ' \
                   'памяти особым образом, поэтому операции с их элементами выполняются заведомо быстрее, чем с ' \
                   'компонентами списка. Безопасность — неизменяемость также позволяет им быть идеальными кандидатами ' \
                   'на роль констант. Константы, заданные кортежами, позволяют сделать код более читаемым и безопасным. ' \
                   'Использование tuple в других структурах данных — кортежи применимы в отдельных структурах данных, ' \
                   'от которых python требует неизменяемых значений. Например ключи словарей (dicts) должны состоять ' \
                   'исключительно из данных immutable-типа.'
    res = ''
    length_in = len(input_phrase)
    
    for i in range(length_in // 2):
        res += input_phrase[i]
    print(res)

    tmp = ''
    
    for i in range(length_in - 1, length_in // 2 - 1, - 1):
        tmp += input_phrase[i]
    print(tmp, '\n')

    output_phrase = ''
    i = 1
    
    for i in range(length_in // 2):
        output_phrase += res[i]
        output_phrase += tmp[i]
    if length_in % 2:
        output_phrase += tmp[i + 1]

    print(f"ШИФР:\n {output_phrase}", '\n')

    corrective = 0
    length_out = len(output_phrase)
    
    if length_out % 2 == 0:
        corrective = 1

    result = output_phrase[0:length_out:2] + output_phrase[length_out - 2 + corrective:0:-2]
    print(f"Зашифрованное слово: {result}",'\n')
