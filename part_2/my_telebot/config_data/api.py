"""
Код реализует взаимодействие с внешним API для работы с переводами
и словарными определениями слов через HTTP-запросы.

Функции делают запрос и возвращают обычные словари или списки, которые отдал сервер.

Обычно в ответе сервера есть много лишней информации, поэтому отсеивать её
лучше прямо в модуле api.py, например, создав класс вида CompleteResult,
который в более удобном виде будет хранить списки синонимов и переводов.
"""

import requests
from typing import List, Dict

from my_telebot.config_data.config import API_KEY, API_BASE_URL


def api_request(endpoint: str, params={}) -> requests.Response:
    """
        api_request:
            Эта функция предназначена для выполнения HTTP GET-запросов к API с определенными параметрами.
            Тут происходит добавление ключа API_KEY к параметрам запроса.
            Затем выполняется GET-запрос к указанному API_BASE_URL с указанными параметрами.

        :param endpoint (строка): точка входа в API.
        :param params (словарь): опциональные параметры запроса.
        :return: Возвращает объект requests.Response, который содержит ответ от API.
        """
    params['key'] = API_KEY
    return requests.get(
        f'{API_BASE_URL}/{endpoint}',
        params=params
    )


def get_langs() -> List[str]:
    """
        Функция вызывает api_request с endpoint='getLangs',
        чтобы получить список доступных языков для перевода.

        :return: Возвращает список строк, представляющих доступные языки.
        """
    response = api_request('getLangs')
    return response.json()


def complete_word(q: str, lang: str, limit: int = 1) -> Dict:
    """
        Возвращает наиболее вероятное продолжение текста, а также признак конца слова.
        Функция выполняет запрос к API для поиска определения слова или фразы в словаре.
        Выполняет api_request с endpoint='complete' и передает параметры языка, текста и интерфейса.

        :param q: Текст, на который указывает курсор пользователя.
        :param lang: Язык текста (например, "en").
        :param limit: Максимальное количество возвращаемых строк (по умолчанию 1).

        :return: Возвращает словарь вида {"endOfWord":false,"pos":-2,"text":["world"]} или пустой словарь {}.
        """
    response = api_request('complete', params={
        'q': q,
        'lang': lang,
        'limit': limit
    })

    return response.json().get('text', {})
