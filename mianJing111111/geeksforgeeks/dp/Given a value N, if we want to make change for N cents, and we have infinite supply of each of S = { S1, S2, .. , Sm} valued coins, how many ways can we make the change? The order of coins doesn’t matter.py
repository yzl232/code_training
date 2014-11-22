# encoding=utf-8
'''


Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.


Dynamic programming problem: Coin change problem: Find the minimum number of coins required to make change for a given sum (given unlimited cumber of N different denominations coin)
'''





class Solution:
    def count(self, values, target):
        if target==0: return 1
        if target<0: return 0
        if len(values)<=0 and target>0:
            return 0
        return self.count(values[1:], target) + self.count(values, target-values[0])
#不要自己。  要自己，target-values[0]

#dp
class Solution2:
    def count(self, values, target):
        m = len(values); n = target
        dp = [[0 for i in range(n+1)] for j in range(len(values))]
        dp[0] = 1
        for i in range(0, m):
            dp[0][i] = 1

        for i in range(1, n+1):
            for j in range(m):
                val = values[j]
                x = dp[i-val][j] if i-val>=0 else 0  #用了这种硬币
                y = dp[i][j-1] if j>=1 else 0 #没用
                dp[i][j] = x+y
        return dp[-1][-1]
