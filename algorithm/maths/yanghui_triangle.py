def triangle(n: int) -> list:
    """
    杨辉三角
    href:
    n: int 层数
    returns: list: 数据列表
    """
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    num = [1]

    for i in range(n):
        for j in range(len(num)-1):
            for s in range(1, len(num)):
                num.append(num[s]+num[j])
                num.append(1)
                continue
        nums = num
    return [[1], [1, 1], num]

if __name__ == "__main__":
    # 输出5层杨辉三角
    triangle(1)

    # 输出10层杨辉三角
    triangle(10)