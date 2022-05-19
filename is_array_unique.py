# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

from collections import Counter


def containsDuplicate(nums):
    c = Counter(nums)
    rep = c.most_common(1)[0][1]
    if rep > 1:
        return True
    else:
        return False


containsDuplicate([0, 2, 3, 4, 5])

# Faster solution:
# def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(nums) > len(set(nums)):
#             return True
#         else:
#             return False
