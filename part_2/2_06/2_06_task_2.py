# Часть 2. Модуль 6. Практическая работа. Задание 2. Криптовалюта
#
# При работе с API (application programming interface) сайта биржи по криптовалюте
# вы получили такие данные в виде словаря:
#
# data = {
# "address": "0x544444444444",
# "ETH": {
# "balance": 444,
# "totalIn": 444,
# "totalOut": 4
# },
# "count_txs": 2,
# "tokens": [
# {
# "fst_token_info": {
# "address": "0x44444",
# "name": "fdf",
# "decimals": 0,
# "symbol": "dsfdsf",
# "total_supply": "3228562189",
# "owner": "0x44444",
# "last_updated": 1519022607901,
# "issuances_count": 0,
# "holders_count": 137528,
# "price": False
# },
# "balance": 5000,
# "totalIn": 0,
# "total_out": 0
# },
# {
# "sec_token_info": {
# "address": "0x44444",
# "name": "ggg",
# "decimals": "2",
# "symbol": "fff",
# "total_supply": "250000000000",
# "owner": "0x44444",
# "last_updated": 1520452201,
# "issuances_count": 0,
# "holders_count": 20707,
# "price": False
# },
# "balance": 500,
# "totalIn": 0,
# "total_out": 0
# }
# ]
# }
# Теперь необходимо обработать эти данные.
#
# Напишите программу, которая выполняет следующий алгоритм действий:
#
# Вывести списки ключей и значений словаря.
# В ETH добавить ключ total_diff со значением 100.
# Внутри fst_token_info значение ключа name поменять с fdf на doge.
# Удалить total_out из tokens и присвоить его значение в total_out внутри ETH.
# Внутри sec_token_info изменить название ключа price на total_price.
# После выполнения алгоритма выводить результат (словарь) не нужно.
#
# Советы и рекомендации
# Если вы достали из словаря список по ключу, то можете применять к нему методы списка.
# Например:
#
# словарь[“список”].append(123)
#
# Python возьмёт из словаря объект по ключу «список» и применит к нему метод append.
# Эта же логика работает с другими типами данных. Например, если вы достали из словаря словарь,
# то к нему можно применять методы словаря, а если достали строку — методы строк.
#
# Чтобы не запутаться, распечатывайте объект, который получаете в данный момент. Также можно распечатать тип объекта:
# print(data)
# print(data[‘ключ’], type(data[‘ключ’]))
# print(data[‘ключ’][0], type(data[‘ключ’][0]))
# и так далее.
#
# Так вы всегда будете понимать, над каким объектом работаете в данный момент.
#
# Что оценивается
# Результат вычислений корректен.
# В коде соблюдается порядок действий алгоритма.
# Не используется других переменных, кроме data.

data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
            },
    "count_txs": 2,
    "tokens": [
                {
            "fst_token_info":
                    {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
                    },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
                },

                {
            "sec_token_info":
                    {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
                    },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
                }
            ]
}

# Вывести списки ключей и значений словаря.
# В ETH добавить ключ total_diff со значением 100.
# Внутри fst_token_info значение ключа name поменять с fdf на doge.
# Удалить total_out из tokens и присвоить его значение в total_out внутри ETH.
# Внутри sec_token_info изменить название ключа price на total_price.
# После выполнения алгоритма выводить результат (словарь) не нужно.

# {"address": "0x544444444444",
# "ETH": {"balance": 444, "totalIn": 444, "totalOut": 4},
# "count_txs": 2,
# "tokens": [{"fst_token_info": {1*}, "balance": 5000, "totalIn": 0, "total_out": 0},
#            {"sec_token_info" : {2*}, "balance": 500, "totalIn": 0, "total_out": 0}]}
#
# {1*} "fst_token_info": {"address": "0x44444", "name": "fdf", "decimals": 0, "symbol": "dsfdsf", "total_supply": "3228562189",
#     "owner": "0x44444", "last_updated": 1519022607901, "issuances_count": 0, "holders_count": 137528, "price": False}
#
# {2*} "sec_token_info": { "address": "0x44444", "name": "ggg", "decimals": "2", "symbol": "fff", "total_supply": "250000000000",
#     "owner": "0x44444", "last_updated": 1520452201,  "issuances_count": 0, "holders_count": 20707, "price": False}

print(f"Вывести списки ключей и значений словаря data:")
for data_key, data_val in data.items():
    print(f"{data_key}: {data_val}")

    if data_key == 'ETH':
        data['ETH'].update({'total_diff': '100'})

    elif data_key == 'tokens':
        tokens_list = data['tokens']

        fst_token_info_dict = tokens_list[0]['fst_token_info']
        fst_token_info_dict['name'] = 'doge'

        token_list_0 = tokens_list[0]
        pop_0 = token_list_0.pop('total_out')
        token_list_1 = tokens_list[1]
        pop_1 = token_list_1.pop('total_out')
        data['ETH']['total_out'] = pop_1

        sec_token_info_dict = tokens_list[1]['sec_token_info']
        sec_token_info_dict['total_price'] = sec_token_info_dict.pop('price')

print(f"\nВ ETH добавить ключ total_diff со значением 100:\n"
      f"{data['ETH']}\n"
      f"\nВнутри fst_token_info значение ключа name поменять с fdf на doge\n"
      f"{data['tokens'][0]}\n"
      f"\nУдалить total_out из tokens:\n"
      f"{data['tokens']}\n"
      f"...и присвоить его значение в total_out внутри ETH:\n"
      f"{data['ETH']}\n"
      f"\nВнутри sec_token_info изменить название ключа price на total_price:\n"
      f"{data['tokens'][1]['sec_token_info']}\n")
