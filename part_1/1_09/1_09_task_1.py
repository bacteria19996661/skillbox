# Модуль 9. Задание 1. «Я стал новым пиратом!»
#
# Пользователь вводит десять слов. Напишите программу, которая определяет,
# сколько из них совпадают со словом «Карамба».
#
# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# программа игнорирует регистр первой буквы К;
# переменные имеют значащие имена, не только a, b, c, d (видео 2.3).

need_word = 'Карамба'
count = 0

for yours_word in range(10):
    yours_word = input('Ваше слово: ')
    if yours_word == need_word:
        count += 1

print(f"\nКол-во верных ответов: {count} \n")