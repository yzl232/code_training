# encoding=utf-8
'''


Maximum difference between two elements such that larger element appears after the smaller number

Given an array arr[] of integers, find out the difference between any two elements such that larger element appears after the smaller number in arr[].

Examples: If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8 (Diff between 10 and 2). If array is [ 7, 9, 5, 6, 3, 2 ] then returned value should be 2 (Diff between 7 and 9)
'''
'''
we take the difference with the minimum element found so far. So we need to keep track of 2 things:
1) Maximum difference found so far (max_diff).
2) Minimum number visited so far (min_element).
'''
#dp
class Solution:
    def maxDiff(self, arr):
        ret = 0;  minN = arr[0]
        for i in range(1, len(arr)):
            minN = min(arr[i], minN)
            ret = max(arr[i]-minN, ret)
        return ret