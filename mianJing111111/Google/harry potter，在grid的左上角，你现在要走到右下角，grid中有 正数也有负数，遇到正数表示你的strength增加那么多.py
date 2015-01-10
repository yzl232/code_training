# encoding=utf-8
'''
假设你是harry potter，在grid的左上角，你现在要走到右下角，grid中有
正数也有负数，遇到正数表示你的strength增加那么多，遇到负数表示strength减少那
么多，在任何时刻如果你的strength小于等于0，那么你就挂了。在一开始你有一定的
初始的strength，现在问这个初始的strength最少是多少，才能保证你能够找到一条路
走到右下角。每一步只能向右或者向下。
'''

#必须全程DP才行。  不能只搞个全局变量
# leetcode  dungeon game


class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, mtx):
        minV = mtx[0][0]
        m=len(mtx); n=len(mtx[0])
        dp= [[0 for j in range(n)] for i in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i==m-1 and j==n-1: dp[i][j]=max(1, 1-mtx[m-1][n-1])
                elif i==m-1:  dp[i][j] = max(dp[i][j+1]-mtx[i][j], 1)
                elif j==n-1: dp[i][j] = max(dp[i+1][j]-mtx[i][j], 1)
                else:dp[i][j] =max( min(dp[i+1][j], dp[i][j+1])  - mtx[i][j],    1)
        return dp[0][0]




'''
minV = 10**10
f(i,j) = max( f(i-1,j), f(i,j-1) ) + grid(i,j) .
初始值f(0,1)=grid(0,1), f(1,0)=grid(1,0)，从(0,0)算到(n-1,m-1).
minV = min(f(i, j), minV)


return 0-minV


class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, mtx):
        minV = mtx[0][0]
        m=len(mtx); n=len(mtx[0])
        dp= [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: t=0
                elif i==0: t = mtx[i][j-1]
                elif j==0: t = mtx[i-1][j]
                else: t = max(mtx[i][j-1], mtx[i-1][j])
                dp[i][j] = t+mtx[i][j]
                minV=min(minV, dp[i][j])
        return max(-minV+1, 1)


'''