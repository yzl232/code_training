# encoding=utf-8
'''

Count set bits in an integer

Write an efficient program to count number of 1s in binary representation of an integer.
'''
'''
Count set bits in an integer
'''
class Solution:
    def coutBits(self, n):
        count = 0
        while n:
            count+=n&2   #就是求binary形式那道题      n&1
            n=n>>1
        return count
