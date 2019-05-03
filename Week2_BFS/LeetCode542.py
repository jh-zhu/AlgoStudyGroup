from collections import deque

'''
Time 29.55%
Memory 42.10% (manipulate on the original matrix)
'''

class Solution:
    def updateMatrix(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        # check exception
        if len(matrix) == 0:
            return [[]]
        if len(matrix[0]) == 0:
            return [[]]

        # fill every non-zero elements with +inf
        # add 0s to our initial deque
        q = deque()
        r,c = len(matrix),len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    q.append((i,j))
                else:
                    matrix[i][j] = float('inf')

        # begin to process q
        while q:

            m,n = q.popleft()
            # check the nearby 4 grids
            for i,j in ((m-1,n),(m+1,n),(m,n-1),(m,n+1)):
                val = matrix[m][n]
                # in range
                if 0<=i<r and 0<=j<c and matrix[i][j] >val:
                    matrix[i][j] = val+1

                    q.append((i,j))

        return matrix
