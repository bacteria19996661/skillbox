import json

from telebot.types import Message

from my_telebot.loader import bot
from my_telebot.config_data.config import BOT_TOKEN, DEFAULT_LANG
from my_telebot.config_data.api import get_langs, complete_word
from my_telebot.states.my_states import States
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


available_langs = get_langs()


@bot.message_handler(commands=['start'])
# Декоратор @bot.message_handler(commands=['start']) указывает боту,
# что функция start должна быть вызвана при получении команды /start от пользователя.
def start(message: Message) -> None:
    """
     Функция-обработчик команды /start в Telegram-боте.
     Когда пользователь отправляет эту команду, выполняется код внутри этой функции.
     Функция отправляет приветственное сообщение и устанавливает начальное состояние
     для дальнейшего взаимодействия пользователя с ботом.

     Функция принимает объект message типа Message.

     bot.send_message отправляет приветственное сообщение пользователю,
     содержащее информацию о возможностях бота Яндекс.Предикатора
     и инструкции о том, как пользоваться командой /set_lang.
     message.chat.id - это идентификатор чата, куда будет отправлено сообщение.

     bot.set_state используется для установки состояния пользователя.
     Устанавливается состояние States.base для пользователя
     с идентификатором message.from_user.id в чате с идентификатором message.chat.id.
     Состояние States.base может использоваться для определения контекста или текущего шага
     взаимодействия с пользователем, что позволяет боту адаптировать свое поведение
     в зависимости от этого состояния.

     :param message: содержит информацию о сообщении, отправленном пользователем,
     включая информацию о чате, отправителе и др.
     """
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    # Создание кнопок для стартовых команд
    markup.add(KeyboardButton('/set_lang'))

    bot.send_message(
        message.chat.id,
        'Привет! Я бот Яндекс.Предикатора. Я умею дополнять вводимые слова и фразы.\n\n'
        f'- /set_lang. Выбрать язык ввода [{DEFAULT_LANG}]\n',
        reply_markup=markup    # добавилась эта строка
    )
    bot.set_state(message.from_user.id, States.base, message.chat.id)


@bot.message_handler(commands=['set_lang'])
# Декоратор указывает, что функция set_lang_command должна быть вызвана
# при получении команды /set_lang от пользователя.
def set_lang_command(message: Message) -> None:
    """
     Функция-обработчик команды /set_lang в Telegram-боте.
     Когда пользователь отправляет эту команду, выполняется код внутри этой функции.
     Функция отправляет сообщение с доступными языками перевода и устанавливает состояние,
     ожидая выбора языка пользователем для дальнейших действий.

     Функция принимает объект message типа Message.

     lang_list = ', '.join(available_langs): Создается строка lang_list,
     которая содержит список доступных языков ввода, преобразованный в строку, разделенную запятыми.
     available_langs - это список строк, представляющих доступные языки для ввода, полученные ранее.

     bot.send_message отправляет сообщение пользователю с перечислением доступных языков ввода,
     чтобы пользователь мог выбрать нужный.

     bot.set_state используется для установки состояния пользователя или чата.
     Тут устанавливается состояние States.lang для пользователя
     с идентификатором message.from_user.id в чате с идентификатором message.chat.id.
     Это состояние использоваться для отслеживания выбора языка пользователем
     и адаптации поведения бота в соответствии с выбранным языком ввода.

     :param message: содержит информацию о сообщении, отправленном пользователем,
     включая информацию о чате, отправителе и др.
     """
    # markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=len(available_langs))
    # #Создание кнопок для каждого доступного языка
    # for lang in available_langs:
    #     markup.add(KeyboardButton(lang))
    # bot.send_message(message.chat.id, 'Выберите один из представленных направлений ввода:', reply_markup=markup)

    lang_list = ', '.join(available_langs)
    bot.send_message(message.chat.id, f'Выберите один из представленных языков ввода:\n\n{lang_list}')

    bot.set_state(message.from_user.id, States.lang, message.chat.id)


@bot.message_handler(state=States.lang)
# Декоратор указывает, что функция set_lang должна быть вызвана,
# когда пользователь находится в состоянии States.lang.
def set_lang(message: Message) -> None:
    """
    Функция-обработчик сообщений, который активируется при наличии определенного состояния
    чата/пользователя (States.lang) в Telegram-боте.
    Когда пользователь находится в состоянии выбора языка (States.lang) и отправляет сообщение,
    выполняется код внутри этой функции.

    Функция принимает объект message типа Message.

    :param message: содержит информацию о сообщении, отправленном пользователем,
    включая информацию о чате, отправителе и др.
    :return:
    """
    chosen_lang = message.text     # Получается текстовое содержимое сообщения,
        # отправленного пользователем, и сохраняется в переменной chosen_lang.
    if chosen_lang not in available_langs:
        # Проверяется, содержится ли выбранный пользователем язык
        # (chosen_lang) в списке доступных языков (available_langs).
        bot.send_message(message.chat.id, 'Такого направления ввода нет. Попробуйте еще раз')
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        # Получается доступ к данным пользователя, сохраненным в контексте чата (к объекту data).
        data['lang'] = message.text
        # Выбранный пользователем язык (chosen_lang) сохраняется в контексте пользователя (в объекте data).

        bot.send_message(message.chat.id, f'Выбрано направление {data["lang"]}')
        # Отправляется сообщение пользователю о том, что выбрано определенное направление перевода.

    bot.send_message(message.chat.id, "Для дополнения напишите /complete")
    # Бот отправляет сообщение с инструкцией пользователю о том,
    # что для завершения фразы нужно написать команду /complete.

    bot.set_state(message.from_user.id, States.base, message.chat.id)


@bot.message_handler(commands=['complete'])
# Декоратор указывает, что функция complete_command_handler должна быть вызвана
# при получении команды /complete от пользователя.
def complete_command_handler(message: Message) -> None:
    """
    Когда бот получает команду /complete, он отправляет сообщение в чат.
    После отправки этого сообщения бот устанавливает состояние (state)
    пользователя как States.complete для данного пользователя,
    идентифицируемого по message.from_user.id в чате с идентификатором message.chat.id.
    :param message: содержит информацию о сообщении, отправленном пользователем,
    включая информацию о чате, отправителе и др.
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    # Создание кнопок для стартовых команд
    markup.add(KeyboardButton('/set_lang'))
    markup.add(KeyboardButton('/complete'))

    bot.send_message(
        message.chat.id,
        'Введите текст или фразу.\n'
        'Для смены языка напишите /set_lang',
        reply_markup=markup
    )
    bot.set_state(message.from_user.id, States.complete, message.chat.id)


@bot.message_handler(state=States.complete)
# Декоратор указывает, что функция complete_state_handle должна быть вызвана,
# когда пользователь находится в состоянии States.complete.
def complete_state_handler(message: Message) -> None:
    """
    Тут реализована логика выполнения поиска (или обработки текста).
    Обработчик сообщений, который реагирует на сообщения от пользователя,
    если он находится в состоянии States.complete,
    установленном предыдущим обработчиком команды /complete.

    Получает данные о состоянии пользователя и чата, используя bot.retrieve_data.
    Затем вызывает функцию complete_word с текстом сообщения пользователя в качестве аргумента.
    Результат поиска (или обработки) конвертируется в формат JSON с помощью json.dumps
    с опциями форматирования, чтобы сделать данные читаемыми.

    Отправляет сообщение с результатом поиска в виде отформатированного JSON в чат
    (bot.send_message(message.chat.id, f'<pre>{json_raw}</pre>', parse_mode='html')).

    После отправки результата бот отправляет в чат сообщение "Введите часть текста или фразы"
    для предложения пользователю продолжить фразу или ввести новый запрос.

    :param message: содержит информацию о сообщении, отправленном пользователем,
    включая информацию о чате, отправителе и др.
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        result = complete_word(q=message.text, lang=data.get('lang', DEFAULT_LANG))
        json_raw = json.dumps(result, ensure_ascii=False, indent=2)
        bot.send_message(message.chat.id, f'<pre>{json_raw}</pre>', parse_mode='html')
    bot.send_message(message.chat.id, 'Введите часть текста или фразы')
