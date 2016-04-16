# encoding=utf-8
'''
Given an unsorted array, trim the array such that twice of minimum is greater than maximum in the trimmed array. Elements should be removed either end of the array.

Number of removals should be minimum.

Examples:

arr[] = {4, 5, 100, 9, 10, 11, 12, 15, 200}
Output: 4
We need to remove 4 elements (4, 5, 100, 200)
so that 2*min becomes more than max.


arr[] = {4, 7, 5, 6}
Output: 0
We don't need to remove any element as
4*2 > 7 (Note that min = 4, max = 8)

arr[] = {20, 7, 5, 6}
Output: 1
We need to remove 20 so that 2*min becomes
more than max

arr[] = {20, 4, 1, 3}
Output: 3
We need to remove any three elements from ends
like 20, 4, 1 or 4, 1, 3 or 20, 3, 1 or 20, 4, 1
'''

'''
A O(n^2) Solution
The idea is to find the maximum sized subarray such that 2*min > max. We run two nested loops, the outer loop chooses a starting point and the inner loop chooses ending point for the current starting point. We keep track of longest subarray with the given property.
'''
#题目说了从两边来trim的. 所以是求subarray的过程.
#暴力是O(n3).  可以优化求min, max的过程。 到O（n2）
class Solution:
    def dpremoval(self, arr):
        ret = (0, -1);  n = len(arr)
        for b in range(n):
            minN, maxN=float('inf'), float('-inf')
            for e in range(b, n):
                minN, maxN = min(arr[e], minN), max(arr[e], maxN)
                if 2*minN <=maxN: break   #因为随着arr变大， min可能变小， max可能变大。
                if e-b>ret[-1]-ret[0]: ret = (b,  e)
        if ret==(0, -1): return
        return arr[ret[0]:ret[1]+1]
s = Solution()
print s.dpremoval([4, 5, 100, 9, 10, 11, 12, 15, 200])
# 类似的用cur sum优化复杂度的有 Maximum sum rectangle in a 2D matrix