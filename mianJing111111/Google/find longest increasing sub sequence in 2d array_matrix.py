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

'''
暴力法为甚么 n2
比如
1234
87 65
9101112

   共走了 n, n-1, ....1  .
'''


# n= n1 * n2
# G家考过。  epic也考过。。。。
#就用word search 暴力   O(n2).   比如
#可以做到O(n) 。 比较巧妙。
# dfs是暴力。  这里是类似memoization的dp。 所以复杂度大大优化
class Solution:
    def solve(self, matrix):
        if not matrix: raise ValueError
        self.m=m= len(matrix);  self.n=n=len(matrix[0])
        self.dp =dp= [[None]*n for j in range(m)]
        self.matrix = matrix;  self.ret = (0, -1, -1)  #长度。 终点i, j
        for i in range(m):
            for j in range(n):
                self.fill(i, j)  #下一步由dp反推
        t, i, j = self.ret ;     s = matrix[i][j]
        while dp[i][j]>1:  #可以用dfs找到所有解答  #根据dp逆推
            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0<=r<=m-1 and 0<=c<=n-1 and dp[r][c] == dp[i][j]-1:  #从终点搜索
                        s+=  matrix[r][c];     i, j= r, c ;    break
        return s[::-1]

    def fill(self, i, j):
        if self.dp[i][j]: return
        t = 1
        for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0<=r<=self.m-1 and 0<=c<=self.n-1 and self.matrix[r][c] > self.matrix[i][j]:   #从起点搜索。
                    self.fill(r, c);    t = max(t, self.dp[r][c]+1)
        self.dp[i][j] = t;     self.ret = max(self.ret, (t, i, j))
# 之所以能够实现fill。在于increase是单向的。   所以一定不会无限循环。

# G家考过一维的 ：   按照给定数组的顺序， A[]=5,6,10,11,15,1,2,3  output=3, 也就是 1，2，3；
#  类似于count and say。    O(n), in place
# 和这道题目一致 Find Height of Binary Tree represented by Parent array。  也是G家考过的题目