# Часть 2. Модуль 5. Практическая работа. Задание 9. Анализ комментариев
#
# Напишите программу, которая считывает строку и выводит количество заглавных
# и строчных букв в строке, используя методы строк.
#
# Программа должна это делать за один проход по строке.
#
# Решение должно быть оформлено в виде функции, которая принимает на вход строку-текст,
# а на выход возвращает два числа (количество заглавных и строчных букв).
#
# Пример:
# text = input("Введите строку для анализа: ")
# uppercase, lowercase = count_uppercase_lowercase(text)
# print("Количество заглавных букв:", uppercase)
# print("Количество строчных букв:", lowercase)
#
# Вывод в консоли:
# Введите строку для анализа: Hello World!
# Количество заглавных букв: 2
# Количество строчных букв: 8
#
# Советы
# Вспомните методы строк, которые изучили. Выберите из них те, которые помогут вам
# выполнить проверку буквы (является ли она заглавной или нет).
# Чтобы вернуть несколько элементов из функции, перечислите их через запятую:
# return a, b

def count_up_low(text):

    count_upper, count_lower = 0, 0

    for el in text:
        if el.isupper():
            count_upper += 1
        elif el.islower():
            count_lower += 1
    return print(f"Заглавных букв: {count_upper}, строчных букв: {count_lower}")



if __name__ == '__main__':

    text = input('Введите строку: ')
    result = count_up_low(text)