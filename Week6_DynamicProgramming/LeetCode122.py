'''
Time 63.91%
Memory 38%


Dynamic Programming:
if you want to sell at time t, what is the optimal cost before t
The optimal cost before t is whether keep holding or get the profit and
start a new one
'''



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = -float('inf')
        profit = 0

        for price in prices:
            profit,cost = max(profit,price+cost),max(cost,profit-price)
        return profit
