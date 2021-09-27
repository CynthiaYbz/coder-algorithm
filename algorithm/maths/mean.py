def mean(input_list: list) -> float:
    """
    平均数
    href:
    input_list: list[int] 数值型数据列表
    returns: float: 平均值
    """
    if not input_list:
        return 0
    return sum(input_list) / len(input_list)


if __name__ == "__main__":
    print(mean([]))
    print(mean([30]))
    print(mean([10, 20, 30, 40, 50]))
