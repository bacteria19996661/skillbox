case_periods = {
    ('2022-06-01 00:00:00', '2022-12-31 23:59:59'): (
        5119, 3714, 9171, 3569, 4297, 3031, 3174, 3339, 3507, 4022, 5787, 7266, 7825, 5515, 7652, 7101, 31435, 30533,
        32502, 29782, 30451, 29586, 29733, 30126, 30371, 30069, 27955, 25961, 25719, 26682, 25551, 25000, 24329, 23812,
        25642, 23634, 23513, 22270, 21759, 21386),
    ('2023-01-01 00:00:00', '2023-01-31 23:59:59'): (
        5576, 3083, 3748, 117427, 9397, 3232, 5360, 3926, 3500, 6627, 24466, 6809, 4074, 265769, 3918),
    ('2023-02-01 00:00:00', '2023-02-28 23:59:59'): (12319, 11966, 109755, 3740, 3564, 19639, 268564, 281037, 4792),
    ('2023-03-01 00:00:00', '2023-03-31 23:59:59'): (
        10100, 9835, 6827, 3761, 8790, 4091, 3599, 264085, 263280, 8626, 3331)
}


def temp_ariph_mean(time_dict):
    time_dict = {key: (sum(val), len(val)) for key, val in time_dict.items() for _ in val}
    return time_dict


def ariph_mean(time_dict):
    summ, n = 0, 0

    for key, val in time_dict.items():
        summ += val[0]
        n += val[1]

    return summ/n


if __name__ == '__main__':
    test_cases = [
        case_periods
    ]

    for some_dict in test_cases:
        # for i, v in temp_ariph_mean(some_dict).items():
        #     print(i, v)

        result = ariph_mean(temp_ariph_mean(some_dict))
        print(f"Среднее арифметическое: {result}")
