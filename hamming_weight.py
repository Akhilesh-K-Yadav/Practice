# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/


class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        m = 1
        count = 0
        while i < 32:
            if (n & m) >= 1:
                count += 1
            i += 1
            m = m << 1
        return count


def main():
    ex = Solution()
    print(ex.hammingWeight(11))


main()
