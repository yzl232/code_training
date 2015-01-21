# encoding=utf-8
'''


Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20




We can get the best price by making a cut at different positions and comparing the values obtained after a cut. We can recursively call the same function for a piece obtained after a cut.

Let cutRoad(n) be the required (best possible price) value for a rod of lenght n. cutRod(n) can be written as following.

cutRod(n) = max(price[i] + cutRod(n-i-1)) for all i in {0, 1 .. n-1}
'''


# dp
class Solution:
    def curRod(self, prices, n):
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] =max (prices[x] + dp[i-x]   for x in range(1, i+1))  #j代表size
        return dp[-1]