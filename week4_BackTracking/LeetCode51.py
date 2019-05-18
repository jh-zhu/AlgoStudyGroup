
'''
Time: 22.86%
memory: 63.76%
'''


class Solution:
    def solve(self,col):
        # end condition
        if col == self.size:
            self.ret.append(self.board.copy())

        # for each row
        for row in range(self.size):
            if self.isSafe(row,col):
                l = list(self.board[row])
                l[col] = "Q"
                self.board[row] = ''.join(l)

                self.solve(col+1)

                l1 = list(self.board[row])
                l1[col] = "."
                self.board[row] = ''.join(l1)

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
        for j in range(min(col,self.size-row-1)):
            if self.board[row+j+1][col-j-1] == "Q":
                return False
        return True


    def solveNQueens(self, n: int) -> List[List[str]]:
        self.size = n
        if n==0:
            return []

        # create an empty board (list of string)
        self.board = ['.'*n]*n

        # a list to store solution
        self.ret = []

        # call recursive solve,from the first column
        self.solve(0)


        return self.ret
