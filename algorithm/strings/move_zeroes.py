def moveZeroes2(self, nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
    return nums


def moveZeroes(nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)

    return nums


if __name__ == "__main__":
    print(moveZeroes([0, 0, 1]))
    print(moveZeroes([0, 1, 0, 3, 0]))
    print(moveZeroes([]))