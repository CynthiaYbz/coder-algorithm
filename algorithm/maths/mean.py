def mean(input_list: list) -> float:
    if not input_list:
        return 0
    return sum(input_list) / len(input_list)

if __name__ == "__main__":
    print(mean([]))
    print(mean([10, 20, 30, 40, 50]))
