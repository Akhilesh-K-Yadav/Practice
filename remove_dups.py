# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        count = 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                count += 1
                nums[l] = nums[r]
            r += 1
        return count
