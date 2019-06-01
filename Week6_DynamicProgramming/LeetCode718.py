'''
Time 10.13%

Memory 22.75%

Caution: [[0]*5]*5, the second is copy by reference (list is a object)

'''

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        status = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        l = 0

        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1] == B[j-1]:
                    status[i][j] = status[i-1][j-1]+1
                l = max(l,status[i][j])

        return l
