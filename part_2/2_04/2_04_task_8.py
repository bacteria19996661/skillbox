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

def c_cipher(message:str, offset:int):
    alpha = [chr(i) for i in range(ord("а"), ord("я") + 1)]    # заполняем список буквами алфавита

    c_cipher_message = [(alpha[(alpha.index(i_mes) + offset) % len(alpha)] if i_mes in alpha else i_mes) for i_mes in message]
    c_cipher_message_str = "".join(c_cipher_message)

    return c_cipher_message_str


if __name__ == '__main__':
    test_cases = [
        ('Это питон'.lower(), 3),
        ('это Питон'.lower(), 56)
    ]

    for message, offset in test_cases:
        print(f"Сообщение: «{message}», сдвиг: {offset}")
        result = c_cipher(message, offset)
        print(f"Зашифрованное сообщение: «{result}»\n")