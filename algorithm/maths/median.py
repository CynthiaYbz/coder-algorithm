import numpy as np


def median(input_list: list) -> float:
    input_list.sort()
    num = len(input_list)
    if num % 2 == 1:
        return input_list[num // 2]
    else:
        return sum(input_list[num // 2 - 1: num // 2 + 1]) / 2


def median2(input_list: list) -> float:
    return np.median(input_list)
    #return np.median(sorted(input_list))


if __name__ == "__main__":
    # print(mean([]))
    print(median([60, 10, 20, 30, 40, 50, 70, 80, 90]))
    print(median2([60, 10, 20, 30, 40, 50, 70, 80, 90]))