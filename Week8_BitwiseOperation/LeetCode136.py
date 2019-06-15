'''
Time: 97.01%
Memory: 50.20%


The bitwise XOR is associative
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a
