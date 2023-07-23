# Модуль 12. Задача 7. Недоделка
#
# Используя шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# def rock_paper_scissors():
#   # Здесь будет игра «Камень, ножницы, бумага»
#
# def guess_the_number():
#   # Здесь будет игра «Угадай число»
#
# def mainMenu():
#   # Здесь главное меню игры
#
# mainMenu():
#   pass
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку и выводит, победил он или проиграл.
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры «Угадай число»:
# программа запрашивает у пользователя число до тех пор, пока он не отгадает загаданное.
#
# Что оценивается
# Игры работают корректно.
# В input содержится корректное приглашение для ввода.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).



import random


def word_ending(count):
    text = ''
    if (count == 1) or ((count > 20) and (count % 10 == 1)):
        text = 'ку'
    elif ((count == 2) or (count == 3) or (count == 4)) or ((count > 20) and ((count % 10 == 2) or (count % 10 == 3) or (count % 10 == 4))):
        text = 'ки'
    else:
        text = 'ок'
    return text


def rock_paper_scissors():
    print('\n','*' * 10, 'Добро пожаловать в игру «Камень, ножницы, бумага»', '*' * 10)

    gamer, score, count = 1, 0, 0

    while gamer:
        count += 1
        rand = int(random.randint(1, 3))

        dict_rps = {
            1 : '«камень»',
            2 : '«ножницы»',
            3 : '«бумага»'
        }

        gamer = int(input('\nДля выхода введите 0.\nВведите «камень» - 1, «ножницы» - 2 или «бумага» - 3: '))

        if gamer == 0:
            break
        elif (rand == 1 and gamer == 2) or (rand == 2 and gamer == 3) or (rand == 3 and gamer == 1):
            print(f"Ваш выбор: {gamer} - {dict_rps.setdefault(gamer)}")
            print(f"Случайный выбор компьютера: {rand} - {dict_rps.setdefault(rand)}")
            print('Вы проиграли!')
        elif (rand == 1 and gamer == 3) or (rand == 2 and gamer == 1) or (rand == 3 and gamer == 2):
            score = score + 1
            print(f"Ваш выбор: {gamer} - {dict_rps.setdefault(gamer)}")
            print(f"Случайный выбор компьютера: {rand} - {dict_rps.setdefault(rand)}")
            print(f"УРА! Вы выиграли {score} раз, сделав {count} попыт{word_ending(count)}.")
        elif rand == gamer:
            print('Ничья!')
        else:
            print('Ошибка ввода! Введите 1, 2 или 3. Для выхода из игры введите 0.')
            mainMenu()
    print('Пока!')
    mainMenu()


def guess_the_number():
    print('\n','*' * 10, 'Добро пожаловать в игру «Угадай число»', '*' * 10)
    print("Компьютер будет загадывать число от 1 до 10. Попробуйте угадать!")

    answer, score, count = 1, 0, 0

    while answer:
        count += 1
        rand = random.randint(1, 10)
        answer = int(input('Для выхода введите 0.\nЧисло загадано. Введи своё предположение: '))

        if answer == 0:
            break
        elif answer == rand:
            score = score + 1
            print(f"Правильно! Ты отгадал {score} раз, сделав {count} попыток.")
        else:
            print('Неверно!')

    print('Пока!')
    mainMenu()


def mainMenu():
    choice = input('\nВо что будем играть?\n1 - «Камень, ножницы, бумага»,\n2 - «Угадай число».\nВаш выбор: ')
    if choice == '1':
        rock_paper_scissors()
    elif choice == '2':
        guess_the_number()
    else:
        print('Ошибка ввода: введите 1 или 2.')
        mainMenu()



mainMenu()
