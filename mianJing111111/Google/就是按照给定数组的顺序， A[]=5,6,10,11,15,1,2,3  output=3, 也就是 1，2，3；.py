# encoding=utf-8
# 就是按照给定数组的顺序， A[]=5,6,10,11,15,1,2,3  output=3, 也就是 1，2，3；
#longest consecutive sequence
#就是最大的consecutive subarray

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, a):
        ret = cur = 1
        for i in range(1, len(a)):
            cur = cur + 1 if a[i]==a[i-1]+1 else 1
            ret = max(ret, cur)
        return ret