# encoding=utf-8
'''
find longest increasing sub sequence in 2d array.
(bit more expl..)
ex: finding length of the snake in snake game
---------
the sequence must not be diagonally.
but it can be any like top-bootm,bottom-left-top ........
increasing means one step
ex: 10,11,12,13 (correct)
12,14,15,20(wrong)
Ex: input: consider 4x4 grid
2 3 4 5
4 5 10 11
20 6 9 12
6 7 8 40

output : 4 5 6 7 8 9 10 11 12


和word search 类似。 DFS

'''
# G家考过。  epic也考过。。。。
#就用word search 暴力   O(n2)
#可以做到O(n) 。 比较巧妙。
class Solution:
    def solve(self, matrix):
        self.m=m= len(matrix);  self.n=n=len(matrix[0])
        self.dp = [[None for i in range(self.n)] for j in range(self.m)]
        self.matrix = matrix
        self.ret = (0, -1, -1)
        for i in range(self.m):
            for j in range(self.n):
                self.fill(i, j)  #下一步由dp反推
        i, j = self.ret[1], self.ret[2]
        s = matrix[i][j]
        while matrix[i][j]>1:  #可以用dfs找到所有解答  #根据dp逆推
            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0<=r<=self.m-1 and 0<=c<=self.n-1:
                    if self.matrix[r][c] == self.matrix[i][j]-1:
                        s+=  matrix[r][c]
                        i, j= r, c
                        break
        return s[::-1]


    def fill(self, i, j):
        t = 1
        for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0<=r<=self.m-1 and 0<=c<=self.n-1:
                if self.matrix[r][c] == self.matrix[i][j]-1:
                    if not self.dp[r][c]: self.fill(r, c)
                    t = max(t, self.dp[r][c]+1)
        self.dp[i][j] = t
        if t>self.ret[0]: self.ret=(t, i, j)
        return t
# 之所以能够实现fill。在于increase是单向的。   所以一定不会无限循环。