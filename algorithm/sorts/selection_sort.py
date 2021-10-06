def selection_sort(input_list: list) -> list:
    """
    选择排序
    href: https://baike.baidu.com/item/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F/9762418?fr=aladdin
    input_list: list 数值型数据列表
    returns: list: 排序后数据列表
    """
    num = 0
    size = len(input_list)
    for i in range(size):
        for j in range(i + 1, size):
            if input_list[j] < input_list[num]:
                num = j
        input_list[i], input_list[num] = input_list[num], input_list[i]
        num = i + 1
    return input_list


if __name__ == "__main__":
    print(selection_sort([]))
    print(selection_sort(["a"]))
    print(selection_sort([3, 2, 2]))
    print(selection_sort([0, 5, 2, 3, 2]))
    print(selection_sort([-23, 0, 6, -4, 34]))

    a = "hello"
    b = "hello"
    print(a is b, a == b) 