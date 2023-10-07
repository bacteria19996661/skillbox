#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy
import numpy as np
import statistics


def create_temp_list(s_list: list, s_k: int, s_const: int) -> list:
    """ Вспомогательная функция для вычисения параметра sd. Собирает элементы определенного диапазона. """
    for el in s_list:
        if el >= s_k + s_const:
            return s_list[s_list.index(s_k):s_list.index(el)]


def create_sigma_list(some_list: list):
    """ Вспомогательная функция для вычисения параметра sd. Собирает все диапазоны в один список. """
    some_list.sort()
    k = some_list[0]
    const = 10 ** (len(str(k)) - 1)
    sigma_list = []

    while k < some_list[-1]:
        temp_sigma_list = create_temp_list(some_list, k, const)
        sigma_list.append(temp_sigma_list)
        # print(temp_sigma_list)
        el = temp_sigma_list[-1]
        some_list = some_list[some_list.index(el) + 1:]
        k = some_list[0]
    return sigma_list


def max_length(s_list):
    """ Вспомогательная функция для вычисения параметра sd. Находит наиболее часто встречающийся диапазон значений. """
    for el in s_list:
        max_len = len(el)
        max_len_el = el
        if len(el) > max_len:
            max_len = len(el)
            max_len_el = el
        return max_len_el


def find_sigma(lst):
    """ Вспомогательная функция для вычисения параметра sd. Находит максимально вероятностный элемент sd. """
    max_list = max_length(lst)
    ind = len(max_list) // 2
    return max_list[ind]


def normal_dist(x, mean, sd):
    """
    Функция вычисляет нормальное распределение.

    :param x: quantiles (90-й процентиль)
    :param mean: Mean of the distribution
    :param sd: Satndard deviation of the distribution
    :return: normal distribution
    """
    prob_density = (np.pi * sd) * np.exp(-0.5 * ((x - mean) / sd) ** 2)
    return prob_density


lst_base = [5119, 3714, 9171, 3569, 4297, 3031, 3174, 3339, 3507, 4022, 5787, 7266, 7825,
            5515, 7652, 7101, 31435, 30533, 32502, 29782, 30451, 29586, 29733, 30126, 30371,
            30069, 27955, 25961, 25719, 26682, 25551, 25000, 24329, 23812, 25642, 23634, 23513,
            22270, 21759, 21386, 5576, 3083, 3748, 117427, 9397, 3232, 5360, 3926, 3500, 6627,
            24466, 6809, 4074, 265769, 3918, 12319, 11966, 109755, 3740, 3564, 19639, 268564,
            281037, 4792, 10100, 9835, 6827, 3761, 8790, 4091, 3599, 264085, 263280, 8626, 3331]

mean = numpy.mean(lst_base) # 33340.04
sd = find_sigma(create_sigma_list(lst_base)) # 3569
x = numpy.quantile(lst_base, 0.9) # 32000
print(f"Диапазон стандартных значений: от {sd} до {x}")

result = normal_dist(x, mean, sd)
print(f"Нормальное распределение: {result}")

# print(f"geometric_mean = {statistics.geometric_mean(lst_base)}")
# print(f"harmonic_mean = {statistics.harmonic_mean(lst_base)}")
# print(f"median = {statistics.median(lst_base)}")
# print(f"mode = {statistics.mode(lst_base)}")
# print(f"multimode = {statistics.multimode(lst_base)}")
# print(f'quantiles = {statistics.quantiles(lst_base)}')
