import telebot
from telebot import custom_filters

from my_telebot.handlers.custom_handlers.my_handlers import *


if __name__ == "__main__":
    """
    Код ниже связан с инициализацией хранилища состояний бота
    и получением списка доступных языков перевода.

    StateMemoryStorage - это хранилище состояний, предоставляемое библиотекой telebot,
    которое позволяет боту отслеживать состояния пользователей или чатов.
    Он используется для хранения информации о текущем состоянии чата или пользователя внутри бота.
    Это может быть полезно, когда вам нужно помнить контекст взаимодействия пользователя
    с ботом для обработки запросов.

    telebot.TeleBot(BOT_TOKEN, state_storage=state_storage) -
    Создание экземпляра класса telebot.TeleBot с передачей токена BOT_TOKEN для инициализации бота.
    Параметр state_storage=state_storage используется для указания хранилища состояний,
    созданного ранее, для отслеживания состояний пользователей или чатов.

    Вызов функции _(). Функция _() использует API для _.
    Переменная _ будет содержать список.
   
    Основные скрипты:
    
    config.py — объявление токенов, ключей и прочих констант;
    states.py — объявление состояний пользователя;
    api.py — работа с API;
    main.py — создание обработчиков и запуск бота.
    """
    try:
        bot.add_custom_filter(custom_filters.StateFilter(bot))
        bot.set_my_commands([    # set_default_commands(bot)
            telebot.types.BotCommand("set_lang", "Сменить язык ввода"),
            telebot.types.BotCommand("complete", "Дополнение слова или фразы")
        ])
        bot.polling()    # bot.infinity_polling()

    except Exception as e:
        print(f"Ошибка запуска бота: {e}")
