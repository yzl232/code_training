# encoding=utf-8
# geeksforgeeks
'''
Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product of lengths of all parts. You must make at least one cut. Assume that the length of rope is more than 2 meters.

Examples:

Input: n = 2
Output: 1 (Maximum obtainable product is 1*1)

Input: n = 3
Output: 2 (Maximum obtainable product is 1*2)

Input: n = 4
Output: 4 (Maximum obtainable product is 2*2)

Input: n = 5
Output: 6 (Maximum obtainable product is 2*3)

Input: n = 10
Output: 36 (Maximum obtainable product is 3*3*4)

1) Optimal Substructure:
This problem is similar to Rod Cutting Problem. We can get the maximum product by making a cut at different positions and comparing the values obtained after a cut. We can recursively call the same function for a piece obtained after a cut.

Let maxProd(n) be the maximum product for a rope of length n. maxProd(n) can be written as following.

maxProd(n) = max(i*(n-i), maxProdRec(n-i)*i) for all i in {1, 2, 3 .. n}

2) Overlapping Subproblems
Following is simple recursive C++ implementation of the problem. The implementation simply follows the recursive structure mentioned above.
'''

#http://www.geeksforgeeks.org/dynamic-programming-set-36-cut-a-rope-to-maximize-product/


# maxProd(n) = max(i*(n-i), maxProdRec(n-i)*i) for all i in {1, 2, 3 .. n}

#和之前这道题目有一点点像
#Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n
class Solution:
    def curRod(self, n):
        dp = [1 for i in range(n+1)]
        for i in range(1, n+1):
            dp[i] =max (  max(j*dp[i-j], (i-j)*j)   for j in range(1, i/2+1))  #j代表size
        return dp[-1]