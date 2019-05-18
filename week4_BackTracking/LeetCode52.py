'''
Same as LeetCode51 N-queens

Time 14.11%
Memory 44.19%
'''
class Solution:
    def solve(self,col):
        # end condition
        if col ==  self.size:
            self.ret+=1

        for row in range(self.size):
            if self.isSafe(row,col):

                l1 = list(self.board[row])
                l1[col] = "Q"
                self.board[row] = ''.join(l1)


                self.solve(col+1)


                l2 = list(self.board[row])
                l2[col] = "."
                self.board[row]= "".join(l2)

    def isSafe(self,row,col):
        # check left
        for j in range(col):
            if self.board[row][j] == "Q":
                return False

        # check upper diagnoal
        for j in range(min(row,col)):
            if self.board[row-j-1][col-j-1] == "Q":
                return False

        # check lower diagnoal
        for j in range(min(self.size-1-row,col)):
            if self.board[row+j+1][col-j-1] == "Q":
                return False

        return True

    def totalNQueens(self, n: int) -> int:
        self.size = n
        self.ret = 0

        # if empty board
        if n==0:
            return ret

        # build a board
        self.board = ['.'*n]*n

        # solve
        self.solve(0)

        return self.ret
