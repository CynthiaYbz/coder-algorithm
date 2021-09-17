import numpy as np

def median(input_list: list) -> float:
    """
    中位数
    href: https://baike.baidu.com/item/%E4%B8%AD%E4%BD%8D%E5%80%BC/9501969?fr=aladdin
    input_list: list[int] 数值型数据列表
    returns: float: 中位值
    """
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
    print(median([60]))
    print(median([60, 10, 20, 30, 40, 50, 70, 80, 90]))
    print(median2([60, 10, 20, 30, 40, 50, 70, 80, 90]))