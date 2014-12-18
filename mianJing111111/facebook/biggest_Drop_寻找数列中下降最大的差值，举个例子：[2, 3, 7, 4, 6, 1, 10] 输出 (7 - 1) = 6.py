# encoding=utf-8
'''
寻找数列中下降最大的差值，举个例子：[2, 3, 7, 4, 6, 1, 10] 输出 (7 - 1) = 6

Find the largest drop (not necessarily adjacent) in an array of integers
'''
class Solution:
    def drop(self, arr):
        if len(arr)<2: return
        result = arr[0]-arr[1]
        maxN = arr[0]
        for i in range(1, len(arr)):
            maxN = max(arr[i], maxN)
            result = max(result,  maxN-arr[i])
        return result
s = Solution()
print s.drop([2, 3, 7, 4, 6, 1, 10])

'''
喝g4g这道题目类似
Maximum difference between two elements such that larger element appears after the smaller number
'''

#dp
class Solution:
    def maxDiff(self, arr):
        if len(arr)<2: return
        ret = arr[1]-arr[0]
        minN = arr[0]
        for i in range(1, len(arr)):
            minN = min(arr[i], minN)
            ret = max(arr[i]-minN, ret)
        return ret