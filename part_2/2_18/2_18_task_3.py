#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 18. Практическая работа. Задача 3. May the force be with you
#
# Фанаты «Звёздных войн» (Star Wars) написали API по своей любимой вселенной. Ссылка на документацию: Documentation.
# Внимательно изучите документацию этого API и напишите программу,
# которая выводит на экран (и в JSON-файл) информацию о пилотах легендарного корабля Millennium Falcon.
# Информация о корабле должна содержать следующие пункты:
# название,
# максимальная скорость,
# класс,
# список пилотов.
# Внутри списка о каждом пилоте должна быть следующая информация:
# имя,
# рост,
# вес,
# родная планета,
# ссылка на информацию о родной планете.

import requests
import json
from typing import Dict
import pprint

req = requests.get('https://swapi.dev/api/starships/')    # отправляем HTTP GET-запрос по указанному URL
if req.status_code == 200:
    data: Dict = json.loads(req.text)
    ship_name: str = 'Millennium Falcon'

    for i_dict in data['results']:
        if i_dict['name'] == ship_name:
            print(f'Корабль {ship_name} найден.')

            data_ship = dict()
            data_ship['ship_name'] = ship_name

            ship_url = i_dict.get('url', None)
            data_ship['ship_url'] = ship_url

            req = requests.get(ship_url)  # отправляем HTTP GET-запрос по указанному URL
            if req.status_code == 200:
                ship: Dict = json.loads(req.text)

                data_ship['starship_class'] = ship['starship_class']
                data_ship['max_atmosphering_speed'] = ship['max_atmosphering_speed']

                pilots_list = list()
                for i_link in ship['pilots']:
                    req = requests.get(i_link)  # отправляем HTTP GET-запрос по указанному URL

                    if req.status_code == 200:
                        pilot: Dict = json.loads(req.text)
                        pilots_list.append({'name': pilot['name'], 'height': pilot['height'], 'mass': pilot['mass'],
                                            'pilots_url': i_link})

                data_ship['pilots'] = pilots_list

                pp = pprint.PrettyPrinter(indent=4)
                pp.pprint(data_ship)

                with open('dataship.json', 'w') as file:
                    data_dump = json.dump(data_ship, file, indent=4)
