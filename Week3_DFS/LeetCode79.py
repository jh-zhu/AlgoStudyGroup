

'''
Time 68.24%
Memory 24.42%

One thing consumed a lot of my time is that, the grid need to be "checked"
after coming across
'''



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not board:
            return False
        r,c = len(board),len(board[0])

        def check(board,word,i,j,k):
            if i< 0 or i>=len(board) or j <0 or j>=len(board[0]) or board[i][j] != word[k] or board[i][j] == "check":
                return False

            # if this is the last word
            if k+1 == len(word):
                return True

            # if not, check around
            c = board[i][j]
            board[i][j] = "check"
            found = check(board,word,i+1,j,k+1) or check(board,word,i-1,j,k+1) or check(board,word,i,j+1,k+1) or check(board,word,i,j-1,k+1)
            board[i][j] = c
            return found


        for i in range(r):
            for j in range(c):
                if check(board,word,i,j,0):
                    return True
        return False
