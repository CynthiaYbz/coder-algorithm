def bubble_sort(input_list: list) -> list:
    """
    冒泡排序
    href: https://baike.baidu.com/item/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F/4602306?fr=aladdin
    input_list: list 数值型数据列表
    returns: list: 排序后数据列表
    """
    size = len(input_list)
    for i in range(size - 1):
        for j in range(size - 1, i, -1):
            if input_list[j] < input_list[j - 1]:
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
    return input_list


if __name__ == "__main__":
    print(bubble_sort([3, 2, 2]))
    print(bubble_sort([0, 5, 2, 3, 2]))
    print(bubble_sort([-23, 0, 6, -4, 34]))
    print(bubble_sort([]))
    print(bubble_sort(["a"]))
    print(bubble_sort(['d', 'a', 'b', 'e', 'c']))