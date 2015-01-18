# encoding=utf-8
'''
3. jumper game: 一个N*N的棋盘，格子里的数字如果是1表示自己棋子，2表示对方棋子，0表示空。放一个棋子到棋盘的空格中，如果相邻上下左右某方向上有对方的棋子，再 过去是空格，则可以跳过对方棋子。同一棋子不能被重复跳过两次。问棋盘上the number of the jumps in the longest path。

    两人下跳棋，给你个位置问你最远能跳多少步。

jumpers

n*n matrix, find the longest ways for each players.
players: red and blue.
players can jump to the next position based on the opposite player, after jump, remove the opposite player.


Given a checker board, find the length of the longest path
  one player can take. You can only make a jump to the left, right, up, or down, and you must have an opponent's piece adjacent to you in that direction and an empty spot after that opponent's piece in the same direction

N*N的 board， 求最大jump over数，给你一个固定位置

'''


#leetcode word search 变种
class Solution:
    def jumpPath(self, matrix, i, j):
        self.jumpNum = 0; self.matrix = matrix
        self.m=len(matrix); self.n = len(matrix[0])
        self.dfs(i, j, 0)
        return self.jumpNum

    def dfs(self, i, j, curN):
        self.jumpNum = max(curN, self.jumpNum)
        for r, c in [(i-2, j), (i+2, j), (i, j-2), (i, j+2)]:
            if 0<=r<=self.m-1 and 0<=c<=self.n-1 and self.matrix[r][c]=='' and self.matrix[(r+i)/2][(c+j)/2] == 'W': # 中间位置是对方
                self.matrix[r][c] ='#'
                self.dfs(r, c, curN+1)
                self.matrix[r][c] = ''