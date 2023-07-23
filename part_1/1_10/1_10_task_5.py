# Модуль 10. Задание 5. Наибольшая сумма цифр
#
# Пользователь вводит N чисел. Среди натуральных чисел, которые он указал,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
#
# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

sequence = input('Введите последовательность чисел через запятую и/или пробел: ')
list_sequence = []

if sequence.find(', '):
    list_sequence = sequence.split(', ')
elif sequence.find(','):
    list_sequence = sequence.split(',')
elif sequence.find(' '):
    list_sequence = sequence.split(' ')

sum_elements = 0
list_sum_elements = []

for elem in list_sequence:
    elem = abs(int(elem))
    while elem > 0:
        sum_elements += elem % 10
        elem = elem // 10
        print(elem)
    list_sum_elements.append(sum_elements)
    sum_elements = 0

#print('Заданная последовательность: ', ListSequence)
#print('Последовательность сумм цифр', ListSumElements)
#print('Максимальная сумма цифр: ', max(ListSumElements))
#print('Индекс числа с максимальной суммой цифр: ', ListSumElements.index(max(ListSumElements)))
#print('Заданной число с этим индексом', ListSequence[ListSumElements.index(max(ListSumElements))])

result = list_sequence[list_sum_elements.index(max(list_sum_elements))]

print(f"Максимальная сумма цифр в последовательности чисел: {max(list_sum_elements)}, число: {result}")
