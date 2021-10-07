def isHappy(n: int) -> bool:
    num = str(n)
    number = 0
    while 1:
        for i in num:
            number += int(i) ** 2

        if number == 1:
            return True
        elif number < 10:
            return False
        else:
            num = str(number)
            number = 0


if __name__ == "__main__":
    print(isHappy(19))
    print(isHappy(5))