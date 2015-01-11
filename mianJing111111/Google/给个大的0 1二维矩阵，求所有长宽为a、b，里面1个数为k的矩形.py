# encoding=utf-8
# 给个大的0 1二维矩阵，求所有长宽为a、b，里面1个数为k的矩形
#做法。 类似于那道容斥原理。

#求和就好了。  sum==k。就是1的个数。
# time: O(n^2), space: O(n^2)
#和那道matrix之和一模一样。 用dp求dp矩阵。
# 用容斥求sub matrix 和
# The SAT is obtained using dp(x,y) = a(x,y) + S(x-1,y) + S(x,y-1) - S(x-1,y-1),
# x = dp[x+a][y+b]- (dp[x+a][y]+dp[x][y+b]-dp[x][y])

class Solution:
    def solve(self, board, a, b, k):
        m = len(board);  n=len(board[0]); cnt=0
        dp = [[0 for i in range(n+1)] for j in range(m+1)]  #多填充了2行。 避免了edge case
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+board[i][j]
                if i>=a and j>=b and dp[i][j]-(dp[i-a][j]+dp[i][j-b]-dp[i-a][j-b])==k:  cnt+=1
        return cnt