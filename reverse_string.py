# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/


def reverseString(s):
    l = len(s)

    lft = 0
    rt = l - 1
    while lft < rt:
        temp = s[lft]
        s[lft] = s[rt]
        s[rt] = temp
        lft += 1
        rt -= 1


s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)
