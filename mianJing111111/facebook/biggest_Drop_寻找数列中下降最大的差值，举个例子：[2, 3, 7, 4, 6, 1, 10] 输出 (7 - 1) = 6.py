# encoding=utf-8
'''
寻找数列中下降最大的差值，举个例子：[2, 3, 7, 4, 6, 1, 10] 输出 (7 - 1) = 6

Find the largest drop (not necessarily adjacent) in an array of integers
'''
class Solution:
    def drop(self, arr):
        maxN = arr[0]; result = -1
        for i in range(1, len(arr)):
            maxN = max(arr[i], maxN)
            result = max(result,  maxN-arr[i])
        return result
s = Solution()
print s.drop([2, 3, 7, 4, 6, 1, 10])

