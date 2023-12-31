# Часть 2. Модуль 8. Практическая работа. Задача 3. Глубокое копирование
#
# site = {
# 'html': {
# 'head': {
# 'title': 'Куплю/продам телефон недорого'
# },
# 'body': {
# 'h2': 'У нас самая низкая цена на iPhone',
# 'div': 'Купить',
# 'p': ‘Продать'
# }
# }
# }
# Напишите программу, которая запрашивает у клиента количество сайтов,
# затем названия продуктов, а после каждого запроса выводит на экран активные сайты.
#
# Условия:
# учтите, что функция должна уметь работать с разными сайтами
# (иначе вам придётся переделывать программу под каждого заказчика заново);
# вы должны получить список, хранящий сайты для разных продуктов
# (а значит, для каждого продукта нужно будет первым делом выполнить глубокое копирование сайта).
# Подсказка
# Чтобы заменить элемент, его нужно найти.
# Для поиска можете использовать рекурсивный алгоритм из задачи по поиску элемента.
#
# Пример вывода
# Сколько сайтов: 2
# Введите название продукта для нового сайта: iPhone
# Сайт для iPhone:
# site = {
# 'html': {
# 'head': {
# 'title': 'Куплю/продам iPhone недорого'
# },
# 'body': {
# 'h2': 'У нас самая низкая цена на iPhone',
# 'div': 'Купить',
# 'p': ‘Продать'
# }
# }
# }
# Введите название продукта для нового сайта: Samsung
# Сайт для iPhone:
# site = {
# 'html': {
# 'head': {
# 'title': 'Куплю/продам iPhone недорого'
# },
# 'body': {
# 'h2': 'У нас самая низкая цена на iPhone',
# 'div': 'Купить',
# 'p': ‘Продать'
# }
# }
# }
# Сайт для Samsung:
# site = {
# 'html': {
# 'head': {
# 'title': 'Куплю/продам Samsung недорого'
# },
# 'body': {
# 'h2': 'У нас самая низкая цена на Samsung',
# 'div': 'Купить',
# 'p': ‘Продать'
# }
# }
# }
# Обратите внимание, что на первой итерации выводится только один сайт (для iPhone),
# а на второй итерации — оба сайта (и для iPhone и для Samsung).
# Чтобы это реализовать, нужно сохранять сайты в списке и каждый раз печатать все его элементы.
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует примеру.
# Input содержит корректные приглашения для ввода.
# Основной функционал описан в отдельной функции(-ях).
# Переменные и функции имеют значимые имена, не только a, b, c, d.

import copy


def deep_copy(some_dict):
    if isinstance(some_dict, dict):
        return {key: deep_copy(value) for key, value in some_dict.items()}
    else:
        return copy.deepcopy(some_dict)


def create_site(site_code, site_name):
    site_copy = deep_copy(site_code)
    site_copy['html']['head']['title'] = f'Куплю/продам {site_name} недорого'
    site_copy['html']['body']['h2'] = f'У нас самая низкая цена на {site_name}'

    return site_copy


def print_dict(some_dict, indent=''):
    for key, value in some_dict.items():
        if isinstance(value, dict):
            print("{indent}{key}: ".format(indent=indent, key=key))
            print_dict(some_dict=value, indent=indent + '   ')
        else:
            print(indent + "{key}: {value}".format(key=key, value=value))


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

num_sites = int(input('Сколько сайтов: '))
sites_list = []
for _ in range(num_sites):
    product = input('\nВведите название продукта для нового сайта: ')
    sites_list.append([f"Сайт для {product}:", create_site(site, product)])
    for el in sites_list:
        print(f"\n{el[0]}")
        print_dict(el[1])
