def plusOne(digits: list) -> list:
    useful_list = []
    useful_str = "".join([str(i) for i in digits])
    useful_list.extend(str(int(useful_str) + 1))
    return [int(i) for i in useful_list]


def plusOne2(digits: list) -> list:
    useful_list = []
    useful_str = "".join(map(str, digits))
    useful_list.extend(str(int(useful_str) + 1))
    return list(map(int, useful_list))


def plusOne3(digits: list) -> list:
    return list(map(int, list(str(int("".join(map(str, digits))) + 1))))


def plusOne4(digits: list) -> list:
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits

if __name__ == "__main__":
    print(plusOne4([9, 9, 8]))
    print(plusOne4([1, 2, 3]))
    print(plusOne3([9, 9, 9]))
    print(plusOne([4, 3, 2, 1]))
    print(plusOne([9]))
    print(plusOne([0]))