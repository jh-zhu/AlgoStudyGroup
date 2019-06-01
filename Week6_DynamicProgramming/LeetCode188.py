'''
Time 40.68%
Memory 40.33%

This is an extension of #124. Be careful that the price list is trival (l==0 or 1)
and the case K is trival or overflowed. If K is greater than l-1, then it is #122,
you can take as many trades as you want

'''




class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k==0:
            return 0

        if not prices or len(prices)==1:
            return 0

        # one problem is that if the n data points only allowing n-1 trades
        # reduce to question 122, can take as many trades as you want
        if k > len(prices)-1:
            cost = -float('inf')
            profit = 0
            for price in prices:
                cost,profit = max(cost,profit-price),max(profit,price+cost)
            return profit



        costs = [-float('inf')]*k
        profits = [0]*k

        for price in prices:
            for i in range(k):
                # update the first case
                if i==0:
                    costs[i],profits[i] = max(costs[i],-price),max(profits[i],costs[i]+price)

                # update remaining k-1 trades
                else:
                    costs[i],profits[i] = max(costs[i],profits[i-1]-price),max(profits[i],price+costs[i])

        return profits[-1]
