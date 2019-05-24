'''
Time 97.41%
Memory 86.30%
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        S = nums[0]
        Smin = min(0,nums[0])
        Vmax = nums[0]

        for i in range(1,len(nums)):
            S += nums[i]
            temp = S-Smin
            if temp > Vmax:
                Vmax = temp
            if S < Smin:
                Smin = S
        return Vmax
