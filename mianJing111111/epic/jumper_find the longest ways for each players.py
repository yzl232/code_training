# encoding=utf-8
'''
3. jumper game: 一个N*N的棋盘，格子里的数字如果是1表示自己棋子，2表示对方棋子，0表示空。放一个棋子到棋盘的空格中，如果相邻上下左右某方向上有对方的棋子，再 过去是空格，则可以跳过对方棋子。同一棋子不能被重复跳过两次。问棋盘上the number of the jumps in the longest path。

似八皇后的递归，两人下跳棋，给你个位置问你最远能跳多少步。

jumpers

n*n matrix, find the longest ways for each players.
players: red and blue.
players can jump to the next position based on the opposite player, after jump, remove the opposite player.


Given a checker board, find the length of the longest path
  one player can take. You can only make a jump to the left, right, up, or down, and you must have an opponent's piece adjacent to you in that direction and an empty spot after that opponent's piece in the same direction

N*N的 board， 求最大jump over数，给你一个固定位置

'''
class Solution:
    def jumpPath(self, matrix, i, j):
        self.jumpNum = 0; self.matrix = matrix
        self.m=len(matrix); self.n = len(matrix[0])
        self.dfs(i, j, 0)
        return self.jumpNum

    def dfs(self, i, j, tmpNum):
        self.jumpNum = max(tmpNum, self.jumpNum)
        if i-2>=0 and (self.matrix[i-1][j]!='' and self.matrix[i-1][j]!=self.matrix[i][j] ) and self.matrix[i-2][j]=='':
            tmp, self.matrix[i][j] = self.matrix[i][j], '#'
            self.dfs(i-2, j, tmpNum+1)
            self.matrix[i][j] = tmp
        if j-2>=0 and (self.matrix[i][j-2]!='' and self.matrix[i][j-1]!=self.matrix[i][j] ) and self.matrix[i][j-2]=='':
            tmp, self.matrix[i][j] = self.matrix[i][j], '#'
            self.dfs(i, j-2, tmpNum+1)
            self.matrix[i][j] = tmp
        if j+2<=self.n and (self.matrix[i][j+2]!='' and self.matrix[i][j+1]!=self.matrix[i][j] ) and self.matrix[i][j+2]=='':
            tmp, self.matrix[i][j] = self.matrix[i][j], '#'
            self.dfs(i, j+2, tmpNum+1)
            self.matrix[i][j] = tmp
        if i+2<=self.m and (self.matrix[i+2][j]!='' and self.matrix[i+1][j]!=self.matrix[i][j] ) and self.matrix[i+2][j]=='':
            tmp, self.matrix[i][j] = self.matrix[i][j], '#'
            self.dfs(i+2, j, tmpNum+1)
            self.matrix[i][j] = tmp