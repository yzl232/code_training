# encoding=utf-8
'''

Find if there is a subarray with 0 sum

Given an array of positive and negative numbers, find if there is a subarray with 0 sum.

Examples:

Input: {4, 2, -3, 1, 6}
Output: true
There is a subarray with zero sum from index 1 to 3.

Input: {4, 2, 0, 1, 6}
Output: true
There is a subarray with zero sum from index 2 to 2.

Input: {-3, 2, 3, 1, 6}
Output: false
There is no subarray with zero sum.

'''
# cumulative sum.    one pass
class Solution:
    def print0S(self, arr):  #非常好的代码。    cumulative sum
        d = {0: -1};  s = 0
        for i in range(len(arr)):
            s+=arr[i]
            if s in d:  return True  #  print arr[d[s]+1:i+1]  #稍作修改
            d[s] = i      #key是cumulative sum
        return False

s = Solution()
print s.print0S([4, 2, 0, 1, 6])
print s.print0S([4, 2, -3, 1, 6])