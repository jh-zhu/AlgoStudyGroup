'''
Time 88.67%
Memory 64.56%

The trick here is seperate all numbers into 2 different groups.
For thoese paired values, the pair should go to the same group.
With in each group, reduce to the original singal number problem

'''


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tmp = 0
        for num in nums:
            tmp ^=num
            # the result of temp is the xor between the 2 only elements

        # find the right most 1 (the place where the 2 only elements begin to different)
        i = 0
        while tmp & 1 ==0:
            tmp >>=1
            i+=1
        tmp = 1<<i

        # seperate into 2 groups, the two only number should go different groups
        first,second = 0,0
        for num in nums:
            # distinguish using the last digit
            if num&tmp:
                first^=num
            else:
                second^=num

        return [first,second]
