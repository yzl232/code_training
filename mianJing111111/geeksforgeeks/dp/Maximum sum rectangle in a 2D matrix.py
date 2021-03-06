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

#leetcode是只有0和1. 找全部是1的。

class Solution:
    def findMaxS(self, mtx):
        if not mtx: return
        ret = float('-inf'); n = len(mtx[0]); m =len(mtx)
        for top in range(m):
            colS = [0]*n       #必须放在这里  . 理解成一直压缩, 压扁成一行colSum
            for bottom in range(top, m):
                for i in range(n):  colS[i]+=mtx[bottom][i]       #新的一行。 压扁。  #这里在求和的时候, 减少了复杂度, 利用了之前的结果
                ret = max(ret, self.maxSubArray(colS))   # 上一行求和不能用list comprehension, 否则会增加复杂度.
        return ret   #类似的还有 Remove minimum elements from either side such that 2*min becomes more than max

    def maxSubArray(self, a):  #leetcode
        ret = maxN = a[0]
        for i in range(1, len(a)):
            maxN = max(maxN + a[i],  a[i])
            ret = max(ret, maxN)
        return ret

matrix =  [[1, 2, -1, -4, -20],
                       [-8, -3, 4, 2, 1],
                       [3, 8, 10, 1, 3],
                       [-4, -1, 1, 7, -6]
                      ]
s = Solution()
print s.findMaxS(matrix)