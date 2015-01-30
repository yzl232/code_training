# encoding=utf-8
'''

给一个2D board，上面由 0 和 1 组成，0 背景，1是图像，求里面有多少个连通域
( Given a matrix with 1's and 0's, find the number of groups
  of 1's. A group is defined by horiz/vertically adjacent 1's )



follow up 是每个连通域的面积是多大。我先写了recursive的做法。

基本上就是leetcode word search
Given a matrix consisting of 0's and 1's, find the largest connected component consisting of 1's.


Iterative 用BFS
'''
#搜索0， 1都不用恢复的


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def findAll(self, board):
        if not board: raise ValueError()
        self.m=m= len(board); self.n = n= len(board[0])
        num=0; sizeArea = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:       #每次找到一个匹配，就迅速把它替换掉。然后DFS
                    board[i][j] = '#'      #比word search要简单。  只要替换过去。 不用替换回来
                    self.size = 0
                    self.dfs(board, i, j)
                    sizeArea.append(self.size)
                    num+=1
        return  num, sizeArea

    def dfs(self, board, i, j):
        self.size+=1
        for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0<=r<self.m and 0<=c<self.n and board[r][c] == 1:
                    board[r][c] = '#'
                    self.dfs(board, r, c)

s = Solution()
a= [ [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1]   ]

print s.findAll(a)