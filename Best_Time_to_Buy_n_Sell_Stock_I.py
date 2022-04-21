# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost_price = 0
        stock = False
        idx = 1
        profit = 0
        while idx < len(prices):
            if prices[idx - 1] > prices[idx]:
                if stock is True:
                    stock = False
                    profit = profit + (prices[idx - 1] - cost_price)

            elif prices[idx - 1] < prices[idx]:
                if stock is False:
                    stock = True
                    cost_price = prices[idx - 1]
            else:
                pass
            idx += 1

        if stock is True:
            stock = False
            profit = profit + (prices[idx - 1] - cost_price)

        return profit
