# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/


class Solution:
    def fizzBuzz(self, n):
        ret_list = []
        i = 1
        while i <= n:
            if (i % 3 == 0) and (i % 5 == 0):
                ret_list.append("FizzBuzz")
            elif i % 3 == 0:
                ret_list.append("Fizz")
            elif i % 5 == 0:
                ret_list.append("Buzz")
            else:
                ret_list.append(str(i))
            i += 1

        return ret_list


def main():
    ex = Solution()
    print(ex.fizzBuzz(4))


main()
