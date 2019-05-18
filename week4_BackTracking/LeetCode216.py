'''
Time 90.40%
Memory 77.97%

Caution that the solution is unique
([1,2,4] is the same as [2,1,4])

'''



class Solution:
    def solve(self,k,index,path):
        # end condition
        if k==0:
            if sum(path) == self.target:
                self.ret.append(path.copy())
            else:
                return
        if index == len(self.l):
            return

        for i in range(index,len(self.l)):
            val = self.l[i]
            if self.isSafe(path,val):
                self.solve(k-1,i+1,path+[val])

    def isSafe(self,path,i):
        return True if sum(path)+i <= self.target else False

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        # candidates
        self.l = [i for i in range(1,10)]
        self.target = n

        self.ret = []


        self.solve(k,0,[])

        return self.ret
