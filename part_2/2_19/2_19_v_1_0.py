#!/usr/bin/python
# -*- coding: utf-8 -*-
# Часть 2. Модуль 19. Видео 1.

import sqlite3

# conn = sqlite3.connect('database.db')
# conn.close()

try:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students;")   # метод  execute возвращает все записи в виде списка кортежей
        print(cursor.fetchall())    # [(2, 'Петр', 'Петров'), (3, 'Анна', 'Петрова')]
        conn.commit()
except Exception as err:
    print(err, type(err))

