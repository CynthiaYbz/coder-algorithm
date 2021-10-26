def isPalindrome(s: str) -> bool:
    result_list = []
    for i in s.upper():
        if i.isalnum():
            result_list.append(i)
    print(result_list)
    for i in range(len(result_list) // 2):
        if result_list[i] != result_list[-i-1]:
            return False
    return True

if __name__ == "__main__":
    #print(isPalindrome("amanaplanacanalpanama"))
    #print(isPalindrome("raceacar"))
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))