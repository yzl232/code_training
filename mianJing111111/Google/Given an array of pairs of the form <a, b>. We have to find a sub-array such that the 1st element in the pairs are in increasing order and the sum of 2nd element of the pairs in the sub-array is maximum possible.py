# encoding=utf-8
'''
Given an array of pairs of the form <a, b>. We have to find a sub-array such that the 1st element in the pairs are in increasing order and the sum of 2nd element of the pairs in the sub-array is maximum possible
'''

def max_sum_sorted(arr):
    if not arr: raise ValueError("empty array")  #一般就是raise ValueError
    ret= maxN = arr[0][1]
    for i in range(1, len(arr)):
        x, y =arr[i]
        maxN = max(y, maxN+y) if x > arr[i-1][0] else y    #主要是多了这一句
        ret = max(maxN, ret)
    return ret


#对比一下原题
class Solution7:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, a):
        result = maxN = a[0]
        for i in range(1, len(a)):
            maxN = max(maxN + a[i],  a[i])
            result = max(result, maxN)
        return result