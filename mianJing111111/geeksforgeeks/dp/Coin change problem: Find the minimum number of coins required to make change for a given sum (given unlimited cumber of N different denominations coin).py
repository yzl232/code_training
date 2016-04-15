# encoding=utf-8
'''
Dynamic programming problem: Coin change problem: Find the minimum number of coins required to make change for a given sum (given unlimited cumber of N different denominations coin)
'''

#复杂度比较差。
class Solution:
    def minCoin(self, arr, target):
        n = target
        dp = [float('inf')]*(n+1)
        dp[0]=0
        for i in range(1, n+1):
            dp[i] = min([dp[i-val]+1 if i-val>=0 else float('inf') for val in arr ])

'''
Greedy algorithm does not always give you minimum number of coins. Consider sum as 40, and coins as {1, 5, 10, 20, 25}.

Greedy algorithm will give:{25, 10, 5}. However the correct answer is {20, 20}. So dynamic programming is one way to solve this.
'''