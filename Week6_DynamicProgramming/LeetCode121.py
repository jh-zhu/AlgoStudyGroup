'''
Time 76.38%
Memory 79.29%

The key idea:
At time t, the best buy time is always the lowest time showed
before time t. Then we can calculate the profit to be made if sell at t
Compare all profits by selling at time t to get the maximum profits

Python tip a,b = b,a to exchange value

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # optimal cost up to time t
        cost = -float('inf')
        # highest profit up to time t
        profit = 0

        for price in prices:
            # optimize cost up to time t, update profit up to time t
            cost,profit = max(cost,-price),max(profit,price+cost)

        return profit\
