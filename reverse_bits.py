# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
class Solution:
    def reverseBits(self, n: int) -> int:
        in_mask, out_mask, out = 1, 2147483648, 0

        for i in range(32):
            if in_mask & n:
                out = out | out_mask
            in_mask = in_mask << 1
            out_mask = out_mask >> 1
        return out


# Fastest solution:
# def reverseBits(self, n: int) -> int:
#         #The 0 in 08b is part of the format specification. See the documentation here. If you want zero padding, do '{0:016b}'.format(6) or '{0:032b}'.format(6).
#         return int("{:032b}".format(n)[::-1],2)
