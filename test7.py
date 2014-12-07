class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return 
        r = len(board); c = len(board[0])
        pre = set([])
        for i in range(r):
            if board[i][0] == 'O': pre.add((i, 0))
            if board[i][c-1] == 'O': pre.add((i, c-1))
        for j in range(c):
            if board[0][j] == 'O': pre.add((0, j))
            if board[r-1][j] == 'O': pre.add((r-1, j))
        while len(pre)>0:
            cur = set([])
            for d in pre:       board[d[0]][d[1]] = '#'
            for can in pre:
                i = can[0]; j = can[1]
                for d in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<=d[0]<=r-1 and 0<=d[1]<=c-1 and board[d[0]][d[1]]=='O': cur.add(d)
            pre = cur
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '#': board[i][j] = 'O'
                
                
'''
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return
        r, c, candidates = len(board), len(board[0]), set([])
        self.r , self.c = r, c
        for i in range(r):
            if board[i][0] == 'O': self.dfs(i, 0, board)
            if board[i][c-1] == 'O':self.dfs(i, c-1, board)
        for i in range(c):
            if board[0][i] == 'O': self.dfs(0, i, board)
            if board[r-1][i] == 'O': self.dfs(r-1, i, board)

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(r):
            for j in range(c):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                    
    def dfs(self, i, j, board):
        board[i][j] = '#'
        if i>0 and board[i-1][j] == 'O': self.dfs(i-1, j, board)
        if i<self.r-1 and board[i+1][j] == 'O': self.dfs(i+1, j, board)
        if j>0 and board[i][j-1] == 'O': self.dfs(i, j-1, board)
        if j<self.c-1 and board[i][j+1] == 'O': self.dfs(i, j+1, board)

'''