from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data.config import BOT_TOKEN

"""
    Инициализация хранилища состояний бота и получение списка доступных языков.
    
    StateMemoryStorage - это хранилище состояний, предоставляемое библиотекой telebot,
    которое позволяет боту отслеживать состояния пользователей или чатов.
    Он используется для хранения информации о текущем состоянии чата или пользователя внутри бота.
    Полезно, когда нужно помнить контекст взаимодействия пользователя с ботом для обработки запросов.
    
    TeleBot(BOT_TOKEN, state_storage=storage) - создание экземпляра класса 
    telebot.TeleBot с передачей токена BOT_TOKEN для инициализации бота.
    Параметр state_storage=storage используется для указания хранилища состояний,
    созданного ранее, для отслеживания состояний пользователей или чатов.
"""
storage = StateMemoryStorage()
bot = TeleBot(token=BOT_TOKEN, state_storage=storage)
