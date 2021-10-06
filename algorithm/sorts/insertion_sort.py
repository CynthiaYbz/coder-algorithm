def insertion_sort(input_list: list) -> list:
    result_list = []
    if input_list:
        result_list.append(input_list[0])
    for i in range(1, len(input_list)):
        for j in range(i-1, -1, -1):
            if input_list[i] > result_list[j]:
                result_list.insert(j+1, input_list[i])
                break
        else:
            result_list.insert(0, input_list[i])
    return result_list

def insertion_sort2(input_list: list) -> list:
    if input_list:
        for i in range(1, len(input_list)):
            for j in range(i, -1, -1):
                if input_list[i] < input_list[j]:
                    input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list

if __name__ == "__main__":
    print(insertion_sort2([]))
    print(insertion_sort2([3, 2, 2]))
    print(insertion_sort2([0, 5, 2, 3, 2]))
    print(insertion_sort2([-23, 0, 6, -4, 34]))
    print(insertion_sort2(['d', 'a', 'b', 'e', 'c']))














