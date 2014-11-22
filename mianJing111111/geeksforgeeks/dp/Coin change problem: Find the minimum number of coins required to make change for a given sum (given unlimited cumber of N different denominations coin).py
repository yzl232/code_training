# encoding=utf-8
'''
Dynamic programming problem: Coin change problem: Find the minimum number of coins required to make change for a given sum (given unlimited cumber of N different denominations coin)
'''

class Solution:
    def minCoin(self, arr, target):
        n = target
        dp = [10**10 for i in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            dp[i] = min(dp[i-val]+1 for val in arr if i-val>=0 )                 #确定取了某种硬币 dp[i-val]+1
        return dp[-1]