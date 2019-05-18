'''
Time 81.23%
Memory 53.50%


The tricky part is the way to think of the sigma algebra
'''


class Solution:
    def find(self,index,path):
        self.ret.append(path)

        for i in range(index,self.n):
            if i == index or self.nums[i] != self.nums[i-1]:
                self.find(i+1,path+[self.nums[i]])

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.nums.sort()
        self.n = len(nums)
        self.path = []
        self.ret = []

        self.find(0,self.path)

        return self.ret
