# Модуль 13. Задача 5. Маятник
#
# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды предыдущего колебания.
# Программа получает на вход начальную амплитуду колебания в сантиметрах
# и конечную амплитуду колебаний, которая считается остановкой маятника.
# Обеспечьте контроль ввода.
#
# Пример:
# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1
# Маятник считается остановившимся через 27 колебаний
#
# Что оценивается
# Результат вывода соответствует условию.
# Input содержит корректное приглашение для ввода.
# Формат вывода соответствует примеру.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).



def input_err(initial_amplitude, amplitude_stop) -> bool:
    return (initial_amplitude <= 0 or amplitude_stop <= 0)


def pendulum(initial_amplitude, amplitude_stop):
    if input_err(initial_amplitude, amplitude_stop):
        raise ValueError("Исходные данные отрицательные либо нулевые.") from None

    attenuation_rate = initial_amplitude
    count = 0
    while attenuation_rate > amplitude_stop:
        attenuation_rate = attenuation_rate - attenuation_rate * 8.4 / 100
        count += 1
    return count



if __name__ == '__main__':
    test_cases = [
        (1, 0.1),    # ожидаем 27
        (10, 0.1),    # ожидаем 53
        (-1, 0)    # ожидаем ошибку
    ]

    try:
        for initial_amplitude, amplitude_stop in test_cases:
            result = pendulum(initial_amplitude, amplitude_stop)
            print(f"Маятник считается остановившимся через {result} колебаний.")
    except Exception as ex:
        print(ex)