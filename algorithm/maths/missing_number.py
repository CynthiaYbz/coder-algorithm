def missingNumber(nums: list) -> int:
    num_set = set(range(len(nums) + 1))
    return list(num_set - set(nums))[0]


if __name__ == "__main__":
    # 你猜别人会怎么做
    print(missingNumber([3, 0, 1]))
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missingNumber([0, 1]))
    print(missingNumber([0]))