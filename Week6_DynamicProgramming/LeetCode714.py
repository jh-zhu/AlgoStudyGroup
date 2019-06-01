'''
Time 74.12%
Memory 22.43%

This is an extension to #122 with transaction fee included

'''


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cost = -float('inf')
        profit = 0
        for price in prices:
            cost,profit = max(cost,profit-price-fee),max(profit,price+cost)

        return profit
