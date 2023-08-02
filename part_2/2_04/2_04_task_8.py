# Часть 2. Модуль 4. Практическая работа. Задание 8. Шифр Цезаря
#
# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась
# на следующую по алфавиту через K позиций по кругу. Если взять русский алфавит и K,
# равное 3, то в слове, которое мы хотим зашифровать, буква А станет буквой Г, Б станет Д и так далее.
#
# Пользователь вводит сообщение и значение сдвига. Напишите программу, которая изменит фразу при помощи шифра Цезаря.
#
# Пример:
# Введите сообщение: это питон.
# Введите сдвиг: 3
# Зашифрованное сообщение: ахс тлхср.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Алгоритм шифрования вынесен в отдельную функцию.
# Переменные и функции имеют значимые имена, не только a, b, c, d.
#
# Чтобы индекс не вышел за пределы списка, нужно ограничить его рост.
# Для этого подходит операция %: (индекс + число) % длина списка.
# Так индекс не будет равен длине списка или не превысит её, а значит не выйдет за пределы списка.
# Например: (id_start + k - 1) % len(people_list)


# Решение skillbox
def skillbox_c_cipher(string, shift):
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'

    char_list = [(alpha[(alpha.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str

# мое решение
def c_cipher(message:str, offset:int):
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    c_cipher_message = []

    for i_mes in message:
        for i, i_al in enumerate(alpha):
            if i_mes == i_al:
                c_cipher_message.append(alpha[(i + offset) % len(alpha)])
            elif i_mes == ' ':
                if ' ' in c_cipher_message:
                    pass
                else:
                    c_cipher_message.append(' ')

    return c_cipher_message



if __name__ == '__main__':
    test_cases = [
        ('это питон', 3),
        ('это питон', 6)
    ]

    for message, offset in test_cases:
        print(f"Сообщение: «{message}», сдвиг: {offset}")
        result = skillbox_c_cipher(message, offset)
        # result = "".join(c_cipher(message, offset))    # для моего решения
        print(f"Зашифрованное сообщение: «{result}»\n")