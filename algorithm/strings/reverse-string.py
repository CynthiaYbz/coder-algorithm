def reverseString(s: list) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s)
    m = n // 2
    for i in range(m):
        s[i], s[n-i-1] = s[n-i-1], s[i]
    return s

def reverseString2(s: list) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n = []
    for i in s[::-1]:
        n.append(i)
    return n

def reverseString3(s: list) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    return s.reverse()

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         n = []
#         for i in s[::-1]:
#             n.append(i)
#         return n

if __name__ == "__main__":
    # print(reverseString(["h", "e", "l", "l", "o"]))
    # print(reverseString(["H", "a", "n", "n", "a", "h"]))
    # print(reverseString3(["H", "a", "n", "n", "a", "h"]))