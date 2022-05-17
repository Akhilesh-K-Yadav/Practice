# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

from pyparsing import nums


def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    # print(nums)
    length = len(nums)
    rotate_by = k % length
    for i in range(rotate_by):
        poped_item = nums.pop(length - 1)
        nums.insert(0, poped_item)


# Fastest solution:
# k=k%len(nums)
# nums[:]=nums[::-1]
# nums[:k] = nums[:k][::-1]
# nums[k:] = nums[k:][::-1]

nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, k=3)
print(nums)
