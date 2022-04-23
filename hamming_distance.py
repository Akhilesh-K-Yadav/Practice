# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        w = x ^ y
        i = 0
        m = 1
        count = 0
        while i < 32:
            if (w & m) >= 1:
                count += 1
            i += 1
            m = m << 1
        return count
