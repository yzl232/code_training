# encoding=utf-8
'''

Dynamic Programming | Set 27 (Maximum sum rectangle in a 2D matrix)

Given a 2D array, find the maximum sum subarray in it. For example, in the following 2D array, the maximum sum subarray is highlighted with blue rectangle and sum of this subarray is 29.
'''

'''
This problem is mainly an extension of Largest Sum Contiguous Subarray for 1D array.

暴力 O(n^4)


Kadane’s algorithm for 1D array can be used to reduce the time complexity to O(n^3). The idea is to fix the left and right columns one by one and find the maximum sum contiguous rows for every left and right column pair. We basically find top and bottom row numbers (which have maximum sum) for every fixed left and right column pair. To find the top and bottom row numbers, calculate sun of elements in every row from left to right and store these sums in an array say temp[]. So temp[i] indicates sum of elements from left to right in row i. If we apply Kadane’s 1D algorithm on temp[], and get the maximum sum subarray of temp, this maximum sum would be the maximum possible sum with left and right as boundary columns. To get the overall maximum sum, we compare this sum with the maximum sum so far.
'''
class Solution:
    def findMaxS(self, matrix):
        if not matrix: return
        ret = -10**10; c = len(matrix[0]); r =len(matrix)
        for top in range(r):
            colSum = [0 for i in range(c)]        #必须放在这里  . 理解成一直压缩, 压扁成一行colSum
            for bottom in range(top, r):
                for i in range(c):
                    colSum[i]+=matrix[bottom][i]       #新的一行。 压扁。
                ret = max(ret, self.maxSubArray(colSum))
        return ret

    def maxSubArray(self, a):  #leetcode
        result = maxN = a[0]
        for i in range(1, len(a)):
            maxN = max(maxN + a[i],  a[i])
            result = max(result, maxN)
        return result

matrix =  [[1, 2, -1, -4, -20],
                       [-8, -3, 4, 2, 1],
                       [3, 8, 10, 1, 3],
                       [-4, -1, 1, 7, -6]
                      ]
s = Solution()
print s.findMaxS(matrix)