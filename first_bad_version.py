# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        h = n
        m = 0
        result = n
        while l <= h:
            m = int((l + h) / 2)
            if isBadVersion(m):
                result = m
                h = m - 1
            else:
                l = m + 1
        return result
