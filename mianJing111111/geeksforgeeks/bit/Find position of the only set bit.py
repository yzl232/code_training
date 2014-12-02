# encoding=utf-8
'''

Find position of the only set bit

Given a number having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit.

其实直接用log2就好了。
'''
class Solution:
    def findPos(self, n):
        cont = 0
        while n:
            n = n>>1
            cont+=1
        return cont