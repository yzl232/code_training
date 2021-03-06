# encoding=utf-8
'''
Write a program for a word search. If there is an NxN grid with one letter in each cell. Let the user enter a word and the letters of the word are said to be found in the grid either the letters match vertically, horizontally or diagonally in the grid. If the word is found, print the coordinates of the letters as output.



Find the presence of a given word in a given grid, word can be matched in any direction up-down, down-up, left-right, right-left, both diagonals up and down etc.

和leetcode差不多。

'''
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, grid, word):
        if not grid or not word: raise ValueError()
        return  any(self.dfs(grid, i, j, word) for i in range(len(grid)) for j in range(len(grid[0])))

    def dfs(self, grid, i, j, word):
        if not word: return True
        if not (0<=i<len(grid) and 0<=j<len(grid[0])) or grid[i][j] != word[0]:  return False     #每次找到一个匹配，就迅速把它替换掉。然后DFS
        t, grid[i][j] = grid[i][j], '#'
        for r in range(i-1, i+2):
            for c in range(j-1, j+2):
                if (r!=i or c!=j) and self.dfs(grid, r, c, word[1:]): return True
        grid[i][j] = t
        return False
'''

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def search(self, board, word):
        if not board or not word: return
        self.m, self.n = len(board), len(board[0])
        self.results = []
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    t, board[i][j] = board[i][j] , '#'
                    self.dfs(board, i, j, word[1:], [(i, j)])
                    board[i][j] = t
        return  self.results

    def dfs(self, board, i, j, word, cur):
        if not word:
            self.results.append(cur)
            return
        for r in [i-1, i, i+1]:
            for c in [j-1, j, j+1]:
                if 0<=r<=self.m-1 and 0<=c<=self.n-1 and board[r][c] == word[0]:
                        tmp, board[r][c] = board[r][c] , '#'
                        self.dfs(board, r, c,word[1:], cur+[(r, c)])
                        board[r][c] = tmp
'''
sss = [
['a', 'b', 'c'], ['c', 'c', 'c']
]
s = Solution()
print s.exist(sss, 'abc')