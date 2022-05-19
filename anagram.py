# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

from typing import Counter


def isAnagram(s, t):
    c_s = Counter(s)
    c_t = Counter(t)
    return c_t == c_s


print(isAnagram("anagram", "xnagaram"))
