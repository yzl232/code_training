
# encoding=utf-8
'''


Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.


Dynamic programming problem: Coin change problem: Find the minimum number of coins required to make change for a given sum (given unlimited cumber of N different denominations coin)



#combination sum的数目。 dp
dfs也可以做。
'''

#先sort values

class Solution:
    def count(self, values, target):
        if target==0: return 1
        if target<0 or not values: return 0
        return self.count(values[1:], target) + self.count(values[:], target-values[0])
#不要自己。  要自己，target-values[0]
#就使用memoization算了。
# dp不是很常规

#dp
class Solution2:
    def count(self, values, target):
        values.sort()
        m = len(values); n = target
        dp = [[0 for j in range(m)] for i in range(n+1)]  #j代表包含valuesd的部分
        for j in range(m):   dp[0][j] = 1  #i=0情况
        for i in range(1, n+1):
            for j in range(1, m):
                v = values[j]
                x = dp[i-v][j] if i-v>=0 else 0  #用了这种硬币
                y = dp[i][j-1] #没用
                dp[i][j] = x+y
        return dp[-1][-1]
