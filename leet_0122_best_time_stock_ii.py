class Solution(object):

    def maxProfit(self, prices):

        max_profit = 0

        for i in range(1, len(prices)):

            if prices[i-1]-prices[i] < 0:
                max_profit = max_profit + (-1*(prices[i-1]-prices[i]))

        return max_profit