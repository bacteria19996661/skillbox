#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 19. Видео 2. Пример запроса
# https://dictionary.yandex.net/api/v1/dicservice.json/getLangs?key=API-ключ
# Ключ: dict.1.1.20231204T072644Z.543c720a9b1b26ed.cb431a76b0c64a171cc2f773a0528c39df54f06e

import requests
import json
from pprint import pprint

API_KEY = 'dict.1.1.20231204T072644Z.543c720a9b1b26ed.cb431a76b0c64a171cc2f773a0528c39df54f06e'
BASE_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json'

def get_langs():
    response = requests.get(f'{BASE_URL}/getLangs', params={
        'key': API_KEY
    })
    return response

def lookup(lang, text, ui='ru'):
    response = requests.get(f'{BASE_URL}/lookup', params={
        'key': API_KEY,
        'lang': lang,
        'text': text,
        'ui': ui
    })
    return response


if __name__ == '__main__':

    langs_response = get_langs()

    if langs_response.status_code != 200:
        print('Не удалось получить список направлений перевода')
        exit(1)

    langs = langs_response.json()
    print('Выберите одно из доступных направлений перевода')
    print(langs)
    while (lang := input('Введите направление: ')) not in langs:
        print('Такого направления нет. Попробуйте ещё раз')

    text = input('Введите слово или фразу для перевода: ')

    lookup_response = lookup(lang, text)

    if lookup_response.status_code != 200:
        print('Не удалось выполнить перевод:', lookup_response.text)
        exit(1)

    try:
        result = pprint(lookup_response.json())
    except UnicodeEncodeError as err:
        print(err)

# req = requests.get(f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={API_KEY}&lang=ru-en&text=задача')
# req = requests.get('https://dictionary.yandex.net/api/v1/dicservice.json/getLangs?key=dict.1.1.20231204T072644Z.543c720a9b1b26ed.cb431a76b0c64a171cc2f773a0528c39df54f06e')
