# encoding=utf-8
'''
Given a NxN matrix which contains all distinct 1 to n^2 numbers, write code to print longest sequence of increasing adjacent sequential numbers.
ex:
1 5 9
2 3 8
4 6 7

should print
6 7 8 9
'''

# 这是O(n4)  有O(n2)解。 用fill dp.

# word search 变体
class Solution:
    # @param board, a list of lists of 1 length string。。
    # @param word, a string
    # @return a boolean
    def exist(self, board):
        self.m, self.n = len(board), len(board[0])
        self.ret = (0, '')
        for i in range(self.m):
            for j in range(self.n):
                t, board[i][j] = board[i][j], -1
                self.dfs(board, i, j, [t])
                board[i][j] = t
        return self.ret

    def dfs(self, board, i, j, cur):
        if len(cur)>self.ret[0]:
            self.ret = (len(cur), cur)
        for r, c in  [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0<=r<=self.m-1 and 0<=c<=self.n-1:
                if board[r][c] ==cur[-1]+1:
                    t, board[r][c] = board[r][c], -1
                    self.dfs(board, r, c, cur+[t])
                    board[r][c] = t

s = Solution()
print s.exist([[1, 5, 9], [2, 3, 8], [4, 6, 7]])

# epic有考这道题目