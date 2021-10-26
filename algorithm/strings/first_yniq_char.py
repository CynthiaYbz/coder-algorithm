def first_yniq_char(s: str) -> int:
    """
    387. 字符串中的第一个唯一字符
    给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
    href: https://leetcode-cn.com/problems/first-unique-character-in-a-string/

    示例：

    s = "leetcode"
    返回 0

    s = "loveleetcode"
    返回 2：

    s: str 数值型数据列表
    int: 索引位置
    """

    for i in range(len(s)):
        count = 0
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                count += 1
                break
        if count > 0:
            continue
        return i
    return -1

def first_yniq_char2(s: str) -> int:
    """
    387. 字符串中的第一个唯一字符
    给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
    href: https://leetcode-cn.com/problems/first-unique-character-in-a-string/

    示例：

    s = "leetcode"
    返回 0

    s = "loveleetcode"
    返回 2：

    s: str 数值型数据列表
    int: 索引位置
    """
    num = list(set(s))
    nums = []
    for i in num:
        n = s.count(i)
        if n == 1:
            nums.append(s.index(i))
    if not nums:
        return -1
    return min(nums)

def firstUniqChar(s: str) -> int:
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
    return -1
if __name__ == "__main__":
    # print(first_yniq_char2("leetcode"))
    # print(first_yniq_char2("leetetl"))
    # print(first_yniq_char2("loveleetcode"))

    print(firstUniqChar("leetcode"))
    print(firstUniqChar("leetetl"))
    print(firstUniqChar("loveleetcode"))
    print(firstUniqChar("aaaaaaaaaaaaaaaaaaaaaaaaaaab"))