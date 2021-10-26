def romanToInt(s: str) -> int:
    """
    罗马数字转整数
    href: https://baike.baidu.com/item/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F/4602306?fr=aladdin
    input_list: list 数值型数据列表
    returns: list: 排序后数据列表
    """
    y = s.lower()
    num = 0
    nums = {"iv": 4, "ix": 9, "xl": 40, "xc": 90, "cd": 400, "cm": 900}
    number = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
    for e in nums.keys():
        count = y.count(e)
        num = num + count * nums[e]
        y = y.replace(e, "")
    for j in number.keys():
        count_2 = y.count(j)
        num = num + count_2 * number[j]
    return num


def romanToInt2(s: str) -> int:
    """
    罗马数字转整数
    href: https://baike.baidu.com/item/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F/4602306?fr=aladdin
    input_list: list 数值型数据列表
    returns: list: 排序后数据列表
    """
    s = s.replace("IV", "4 ")
    s = s.replace("IX", "9 ")
    s = s.replace("XL", "40 ")
    s = s.replace("XC", "90 ")
    s = s.replace("CD", "400 ")
    s = s.replace("CM", "900 ")
    s = s.replace("I", "1 ")
    s = s.replace("V", "5 ")
    s = s.replace("X", "10 ")
    s = s.replace("L", "50 ")
    s = s.replace("C", "100 ")
    s = s.replace("D", "500 ")
    s = s.replace("M", "1000 ")
    s.split()
    l = list(s)
    return sum(map(int, l))

def romanToInt3(s: str) -> int:
    """
    罗马数字转整数
    href: https://baike.baidu.com/item/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F/4602306?fr=aladdin
    input_list: list 数值型数据列表
    returns: list: 排序后数据列表
    """

    pass





if __name__ == "__main__":
    print(romanToInt2("III"))
    print(romanToInt2("IV"))
    print(romanToInt2("LVIII"))
    print(romanToInt2("MCMXCIV"))