import random


class Solution:
    def __init__(self, nums):
        self.orig = list(nums)
        self.aux = nums

    def reset(self):
        return self.orig

    def shuffle(self):
        length = len(self.aux)
        i = length - 1
        while i > 0:
            rand_idx = random.randint(0, i)
            temp = self.aux[rand_idx]
            self.aux[rand_idx] = self.aux[i]
            self.aux[i] = temp
            i -= 1
        return self.aux


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_1 = obj.reset()
print(param_1)
