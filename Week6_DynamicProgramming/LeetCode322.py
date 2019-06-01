'''
Time 31.29%
Memory 69.75%

if there is n way of making amount-coin, the way
to make amount is min(way,way(amount-coin)+1)

'''



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [-1] * (amount+1)

        # you can always make it buy giving 0 coins
        # -1 means you can never make it
        res[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i >= coin and res[i-coin]>-1:
                    if res[i] == -1:
                        res[i] = res[i-coin] +1
                    else:
                        res[i] = min(res[i],res[i-coin]+1)
        return res[amount]
