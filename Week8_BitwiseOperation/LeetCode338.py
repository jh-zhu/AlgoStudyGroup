'''
Time 92.96%
Memory 77.84%

The trick is to count the rightmost bit:
if it is 1, add 1 to the counting with 1 right shift
otherwise add 0

'''


class Solution:
    def countBits(self, num: int) -> List[int]:
        count = [0]
        for i in range(1,num+1):
            count.append(count[i>>1]+(i&1))
        return count
