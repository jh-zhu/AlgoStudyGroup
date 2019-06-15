'''
Time 90.59%
Memory 91.84%

An array of element n has 2**n subsets,corresponding to
a binary number of n bits. Add elements of subsets guided by
all the binary numbers

'''




class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        counts = 2**len(nums)

        for count in range(counts):
            temp = []
            for i,n in enumerate(nums):
                if count & 1<<i >0:
                    temp.append(n)
            res.append(temp)
        return res
