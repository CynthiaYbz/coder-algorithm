import pandas as pd


def mode(input_list: list) -> list:
    """
    众数
    href: https://baike.baidu.com/item/%E4%BC%97%E6%95%B0/44796
    input_list: list 数值型数据列表
    returns: 众数列表
    """
    if not input_list:
        return []

    input_set_list = list(set(input_list))
    count_dict = dict()
    for value in input_set_list:
        count_dict[value] = input_list.count(value)
    num = max(list(count_dict.values()))

    return [key for key, value in count_dict.items() if num == value]


def mode_pandas(input_list: list) -> list:

    return pd.Series(input_list).mode().to_list()


if __name__ == "__main__":
    # print(mode([]))
    print(mode([60]))
    print(mode([60, 60]))
    print(mode([10, 10, 20, 30, 40, 10, 70, 80, 90]))
    print(mode([60, 10, 20, 10, 40, 50, 70, 50, 90]))