# Часть 2. Модуль 10. Практическая работа. Задача 4. Чат
#
# Реализуйте программу — чат, в котором могут участвовать сразу несколько человек,
# то есть программу, которая может работать одновременно для нескольких пользователей.
# При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
#
# Посмотреть текущий текст чата.
# Отправить сообщение (затем вводит сообщение).
# Действия запрашиваются бесконечно.
#
# Примечание: для решения задачи вам достаточно текущих знаний, нужно лишь проявить
# немного фантазии и хитрости. Не углубляйтесь в дебри работы с сетями, создание GUI-приложений и прочее.
# Однако, если очень хочется, то останавливать вас никто не будет!
#
# Что оценивается
# Результат вычислений корректен.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
# Входные и выходные файлы названы так, как указано в задании.
# Сообщения об ошибках осмысленные и понятные для пользователя.


# МОЕ РЕШЕНИЕ:

import os
def action(name):
    user_choose = input(f"\nВыберите действие:\n"
                        f"2 - посмотреть чат\n"
                        f"3 - отправить сообщение\n"
                        f"{name}, ваш выбор: ")

    match user_choose:

        case '2':
            with open('messages.txt', 'r', encoding='utf-8') as file_r:
                if os.stat('messages.txt').st_size != 0:
                    for line in file_r:
                        print(''.join(line), end='')
                else:
                    print('Служебное сообщение: пока ничего нет.\n')
        case '3':
            message = input("Введите сообщение: \n")
            if message == '':
                raise Exception('Нельзя оставлять пустое сообщение.')
            with open('messages.txt', 'a', encoding='utf-8') as file_w:
                file_w.write('{name}: {message}\n'.format(name=name, message=message))
        case 'exit':
            exit()
        case _:
            print('Команда не распознана. Повторите.')


def all_users_status():
    print("Пользователи чата:")
    for key, val in users_dict.items():
        print(f"{key}: {val}")


if __name__ == '__main__':
    try:
        with open('messages.txt', 'w+', encoding='utf-8') as file_massages:
            file_massages.seek(0)
    except (FileNotFoundError, FileExistsError) as exc:
        print(exc, type(exc))

    users_dict = {}

    while True:
        user_name = input("Введите имя пользователя: ")
        if user_name == '':
            raise Exception('Нельзя использовать пустое имя.')
        print(f"{user_name}, добро пожаловать в чат!\n")
        users_dict[user_name] = 'Online'
        all_users_status()

        user_exit = '0'
        while user_exit != '1':

            try:
                action(user_name)
            except (FileNotFoundError, FileExistsError) as err:
                print(err, type(err))

            user_exit = input(f"\n1 - выйти из чата"
                              f"\n0 - продолжить"
                              f"\nexit - завершить программу"
                              f"\n{user_name}, ваш выбор:")
            if user_exit == '1':
                print(f"Пока,{user_name}!\n")
                users_dict[user_name] = 'Offline'
                break
            elif user_exit == 'exit':
                exit()


# Решение Skillbox
# import time
#
# user_name = input('Введите имя пользователя: ')
# while True:
#     print('')
#     response = input('Введите 1 или 2: ')
#     if response == '1':
#         try:
#             with open('chat.txt', 'r') as file:
#                 messages = file.readlines()
#                 print(''.join(messages))
#         except FileNotFoundError:
#             print('Служебное сообщение: пока ничего нет.\n')
#     elif response == '2':
#         new_message = input('Введите сообщение: ')
#         with open('chat.txt', 'a') as file:
#             file.write('{name}: {message}\n'.format(
#                 name=user_name, message=new_message))
#     else:
#         print('Неизвестная команда.\n')