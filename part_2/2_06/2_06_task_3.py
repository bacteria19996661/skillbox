# Часть 2. Модуль 6. Практическая работа. Задание 3. Товары
#
# В базе данных магазина вся необходимая информация по товарам делится на два словаря:
# первый отвечает за артикулы, второй — за списки количества товаров на складе:
#
# goods = {
# 'Лампа': '12345',
# 'Стол': '23456',
# 'Диван': '34567',
# 'Стул': '45678',
# }
# store = {
# '12345': [
# {'quantity': 27, 'price': 42},
# ],
# '23456': [
# {'quantity': 22, 'price': 510},
# {'quantity': 32, 'price': 520},
# ],
# '34567': [
# {'quantity': 2, 'price': 1200},
# {'quantity': 1, 'price': 1150},
# ],
# '45678': [
# {'quantity': 50, 'price': 100},
# {'quantity': 12, 'price': 95},
# {'quantity': 43, 'price': 97},
# ],
# }
# Каждая запись второго словаря отображает, сколько и по какой цене
# закупалось товаров. Цена указана за одну штуку.
# Напишите программу, которая рассчитывает общую стоимость позиций
# для каждого товара на складе и выводит эту информацию на экран.
#
# Результат работы программы:
# Лампа — 27 штук, стоимость 1134 рубля.
# Стол — 54 штуки, стоимость 27 860 рублей.
# Диван — 3 штуки, стоимость 3550 рублей.
# Стул — 105 штук, стоимость 10 311 рублей.
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует указанному в задаче.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

def get_key(val):
    for key, value in goods.items():
        if val == value:
            return key
    return "key doesn't exist"

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
            ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
            ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
            ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
            ],
}

quantity_sum, price_sum = 0, 0

for s_key, s_val in store.items():
    prod = get_key(s_key)
    for i_store in store[s_key]:
        quantity_sum += i_store['quantity']
        price_sum += i_store['price'] * i_store['quantity']

    # match end_1:
    #     case (quantity_sum % 10 == 1):
    #         end_1 = 'а'
    #     case (quantity_sum % 10 == 2) or (quantity_sum % 10 == 3) or (quantity_sum % 10 == 4):
    #         end_1 = 'и'
    #     case _:
    #         end_1 = ''
    #
    # match end_2:
    #     case (price_sum % 10 == 1):
    #         end_2 = 'ь'
    #     case (price_sum % 10 == 2) or (price_sum % 10 == 3) or (price_sum % 10 == 4):
    #         end_2 = 'я'
    #     case _:
    #         end_2 = 'ей'

    if quantity_sum % 10 == 1:
        end_1 = 'а'
    elif quantity_sum % 10 == 2 or quantity_sum % 10 == 3 or quantity_sum % 10 == 4:
        end_1 = 'и'
    else:
        end_1 = ''

    if price_sum % 10 == 1:
        end_2 = 'ь'
    elif price_sum % 10 == 2 or price_sum % 10 == 3 or price_sum % 10 == 4:
        end_2 = 'я'
    else:
        end_2 = 'ей'

    print("{prod} -- {quantity_sum} штук{end_1}, стоимость {price_sum:,d} рубл{end_2}.".format(
        prod=prod, quantity_sum=quantity_sum, end_1=end_1, price_sum=price_sum, end_2=end_2))
    num = 456767

    quantity_sum, price_sum = 0, 0

