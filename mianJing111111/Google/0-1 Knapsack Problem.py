# encoding=utf-8
'''
0-1 Knapsack Problem

Given weights and values of n items, put these items in a knapsack of capacity C to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).



#http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
'''

class Solution:
    def dfs(self, weight, vals, c):
        self.weight = weight;  self.vals = vals
        return self.dfs(len(weight)-1, c)

    def dfs(self, i, c):
        if i<0: return 0
        if self.weight[i]>c:  return self.dfs(i-1, c)
        return max(self.dfs(i-1, c),  self.dfs(i-1, c-self.weight[i]))


#dp
class Solution:
    def knapSack(self, weight, vals, c):
        m = len(vals);  n=len(weight)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(n+1):
            for j in range(m+1):
                if weight[i-1]<=c:  dp[i][j] = max(vals[i-1]+dp[i-1][c-weight[i-1]],  dp[i-1][j])
                else:  dp[i][j] = dp[i-1][j]
        return dp[-1][-1]