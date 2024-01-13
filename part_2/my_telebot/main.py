import telebot
from telebot import custom_filters

from my_telebot.handlers.custom_handlers.my_handlers import *


if __name__ == "__main__":
    """
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
