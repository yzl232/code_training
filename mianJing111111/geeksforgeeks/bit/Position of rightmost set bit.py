# encoding=utf-8
'''

Position of rightmost set bit

Write a one line C function to return position of first 1 from right to left, in binary representation of an Integer.
'''
import math
class Solution:
    def find(self, x):
        return int(math.log(x&(~(x-1)), 2))    #x&(x-1) 是把最右边的1置0， x&(~(x-1))

s = Solution()
print s.find(12)