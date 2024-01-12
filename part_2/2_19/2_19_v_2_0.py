#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 19. Видео 2.

# Простейший бот выглядит так:
# На команды /start и /help он ответит любимым приветствием. А на всё остальное повторит то, что написал пользователь.

import telebot
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(massage):
    bot.reply_to(massage, "Hello, World!")

@bot.message_handler(func=lambda message: True)
# Сообщение обработается с помощью обработчика сообщений echo_all.
# Должен быть объявлен после всех обработчиков.
# Функция func может быть более сложной
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.infinity_polling()

    # bot.send_message(message.chat.id, 'Новое сообщение!')    # Команда для отправки сообщения

    # @bot.message_handler(commands=['start'])
    # def welcome(message):
    #     mesg = bot.send_message(message.chat.id, 'Введите имя')
    #     bot.register_next_step_handler(mesg, test)    # обработчик следующего действия пользователя для ввода данных
    #
    # def test(message):
    #     name = message.text
    #     bot.send_message(message.chat.id, f'Ваше имя: {name}')
    #

    # .env (файл с переменными окружения) хранит токены

