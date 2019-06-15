class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            count = 0
            for n in nums:
                count+=(n>>i)&1
            rem = count%3
            if i==31 and rem:
                print(result)
                result -= 1<<31
            else:
                result|= rem<<i

        return result
