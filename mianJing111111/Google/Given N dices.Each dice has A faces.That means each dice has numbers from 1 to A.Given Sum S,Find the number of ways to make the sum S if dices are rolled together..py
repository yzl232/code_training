# encoding=utf-8
'''
Given N dices.Each dice has A faces.That means each dice has numbers from 1 to A.Given Sum S,Find the number of ways to make the sum S if dices are rolled together.
'''

#http://www.geeksforgeeks.org/dice-throw-problem/

'''
Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. X is the summation of values on each face when all the dice are thrown.

The Naive approach is to find all the possible combinations of values from n dice and keep on counting the results that sum to X.


'''
pass


'''
Let the function to find X from n dice is: Sum(m, n, X)
The function can be represented as:
Sum(m, n, X) = Finding Sum (X - 1) from (n - 1) dice plus 1 from nth dice
               + Finding Sum (X - 2) from (n - 1) dice plus 2 from nth dice
               + Finding Sum (X - 3) from (n - 1) dice plus 3 from nth dice
                  ...................................................
                  ...................................................
                  ...................................................
              + Finding Sum (X - m) from (n - 1) dice plus m from nth dice

So we can recursively write Sum(m, n, x) as following
Sum(m, n, X) = Sum(m, n - 1, X - 1) +
               Sum(m, n - 1, X - 2) +
               .................... +
               Sum(m, n - 1, X - m)
'''

class Solution:
    def findWays(self, m, n, x):  #m算是固定值。 主要是x, n
        dp = [[0 for i in range(x+1)] for j in range(n+1)]
        for j in range(1, m+1):
            if j>x: break  #防止越界
            dp[1][j] = 1
        for i in range(2, n+1):
            for j in range(1, x+1):
                dp[i][j]=  sum(dp[i-1][j-k]  for k in range(1, m+1) if j-k>=0)   #防止越界
        return dp[-1][-1]

s = Solution()
print s.findWays(4, 2, 1)
print s.findWays(2, 2, 3)