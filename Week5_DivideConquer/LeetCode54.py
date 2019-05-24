'''
Time 96.41%
Memory 59.39%
'''



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix)==0:
            return []

        res = []
        r1,r2,c1,c2 = 0,len(matrix)-1,0,len(matrix[0])-1

        def divide(r1,r2,c1,c2):
            for c in range(c1,c2+1):
                yield r1,c
            for r in range(r1+1,r2+1):
                yield r,c2

            if c1 < c2 and r1<r2:
                for c in range(c2-1,c1-1,-1):
                    yield r2,c
                for r in range(r2-1,r1,-1):
                    yield r,c1

        while r1<=r2 and c1<=c2:
            for i,j in divide(r1,r2,c1,c2):
                res.append(matrix[i][j])
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return res
