# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/


def firstUniqChar(s):
    length = len(s)
    i = 0
    j = 0
    while i < length:
        while j < length:
            if s[i] == s[j]:
                if i != j:
                    break

            j += 1
        if j == length:
            return i
        i = i + 1
        j = 0
    return -1


#         dict_s = {}
#         for c in s:
#             if dict_s.has_key("c"):
#                 dict_s["c"] = dict_s.get("c") + 1
#             else:
#                 dict_s["c"] = 1


# # Solution 1:
# dict = Counter(s)
# for char in s:
#     if dict[char] == 1:
#         return s.index(char)
# return -1
