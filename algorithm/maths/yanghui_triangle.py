def triangle(n: int) -> list[int]:
    """
    杨辉三角
    href:
    n: int 层数
    returns: list: 数据列表
    """
    n = n + 1
    return [2, 3]


if __name__ == "__main__":
    # 输出5层杨辉三角
    triangle(5)

    # 输出10层杨辉三角
    triangle(10)