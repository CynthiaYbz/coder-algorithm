def fizzBuzz(n: int) -> list:
    result_list = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result_list.append("Fizzbuzz")
        elif i % 5 == 0:
            result_list.append("Buzz")
        elif i % 3 == 0:
            result_list.append("Fizz")
        else:
            result_list.append(str(i))
    return result_list


if __name__ == "__main__":
    print(fizzBuzz(19))
    print(fizzBuzz(150))
    print(fizzBuzz(3))