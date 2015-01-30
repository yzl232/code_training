# encoding=utf-8
'''
Given an array of integers. Find two disjoint contiguous sub-arrays such that the absolute difference between the sum of two sub-array is maximum.
* The sub-arrays should not overlap.

eg- [2 -1 -2 1 -4 2 8] ans - (-1 -2 1 -4) (2 8), diff = 16

I gave him o(n^2) algorithm but he was not satisfied.


'''
#就是用maximum continuous subarray的变体
#因为题目说了是连续子序列。 所以可以O(n)。 如果是sequence那种，只有暴力了。
'''
An O(n) solution is possible.

We consider all "split points", i.e. points such that one subarray lies to the left of it, and one to the right, and compute the best for each possible split point.

Dynamic programming works.

Given Array A[1,...n]

Using the standard dynamic programming algorithm, we can compute for a given i, the maximum and minimum sum subarrays in A[1...i] and A[i+1 ... n]. Note that the point between i and i+1 is a split point.

This can be done by making two passes once from 1 to n, and other from n to 1 and give us four arrays with the max and min sub-array sums.

Now given the above four arrays, for split point between i and i+1, we can take the max and min combinations (max from right, min from left and max from left, min from left), and get the combination which gives the better result.

Once we have the max for each split point, we get the global optimum.

O(n) time, O(n) space.
'''


#四个辅助矩阵
class Solution:
    def solve(self, arr):
      assert len(arr)>=2
      lMin, lMax = self.left_min_max(arr)
      rMin, rMax = self.left_min_max(arr[::-1])  #这一招巧妙
      rMin, rMax = rMin[::-1], rMax[::-1]
      return  max(max(lMax[i-1]-rMin[i], rMax[i] - lMin[i-1]) for i in range(1, len(arr)))  #要么左边比右边大。要么右边比左边大
#边界， i-1, i  。 所以是从1~len(arr)
    def left_min_max(self, a):
        s1 = a[:]; s2=a[:]
        for i in range(1, len(a)):
            s1[i] = max(s1[i-1]+a[i],  a[i])
            s2[i] = min(s2[i-1]+a[i], a[i])
        return s2, s1



s = Solution()
arr = [2, -1, -2, 1, -4, 2, 8]
print(arr, s.solve(arr))
arr = [8, 1, 1, 1]
print(arr, s.solve(arr))
arr = [4, -1, 7]
print(arr, s.solve(arr))