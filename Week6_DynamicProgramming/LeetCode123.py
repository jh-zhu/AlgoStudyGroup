'''
Time 92.73%
Memory 35.29%

This is a combination of #121 and # 122

'''




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost1 = -float("inf")
        profit1 = 0

        cost2 = -float('inf')
        profit2 = 0

        for price in prices:
            # update the first trade
            cost1,profit1 = max(cost1,-price),max(profit1,price+cost1)
            # update the second trade
            cost2,profit2 = max(cost2,profit1-price),max(profit2,price+cost2)

        return profit2
