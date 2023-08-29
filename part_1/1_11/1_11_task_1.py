# Часть 1. Модуль 11. Задача 1. Конвертация
#
# Напишите программу, которая получает на вход стоимость покупки в евро,
# а затем выводит ответ в рублях. Представим, что мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 руб.
#
# Что оценивается
# Результат вывода соответствует условию.
# Input содержит корректное приглашение для ввода.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

def is_exist(price_euro: float) -> bool:
    return price_euro < 0

def currency_converter(price_euro: float) -> float:
    if is_exist(price_euro):
        raise ValueError(f"Отрицательной цены не существует.")

    price_euro = round(price_euro, 2)
    coef_ed = 1.25
    coef_dr = 60.87

    price_dollar = coef_ed * price_euro
    price_rub = coef_dr * price_dollar

    return round(price_rub, 2)


if __name__ == '__main__':
    test_cases = [
        (-1),
        (0),
        (1),
        (10),
        (2.5),
        (12.81)
    ]

    for price_euro in test_cases:
        try:
            result_price = currency_converter(price_euro)
            print(f"Стоимость товара в евро - {price_euro} EU, в рублях - {result_price} RUB.")
        except ValueError as e:
            print(e)
