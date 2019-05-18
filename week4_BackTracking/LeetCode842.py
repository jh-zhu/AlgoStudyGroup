
'''
Time 72.13%
Memory 13.14%

The tricky part for me is that, there could not be numbers with leading 0, but 0
is still a valid number to go into the path
'''


class Solution:
    def solve(self,index):
        if index == self.n and len(self.path) >=3:
            self.ret = self.path.copy()
            return


        for i in range(index,self.n):
            val = int(self.S[index:i+1])
            if val >2**31-1:
                return


            if self.isFibo(self.path,val):
                self.path.append(val)
                self.solve(i+1)
                self.path.pop()

            if val==0:
                return

    def isFibo(self,path,val):
        return True if len(path) < 2 or val == path[-1] + path[-2] else False

    def splitIntoFibonacci(self, S: str) -> List[int]:
        self.S = S
        self.n = len(S)
        self.ret = []
        self.path = []

        self.solve(0)

        return self.ret
