# encoding=utf-8
'''
Program to count number of set bits in an (big) array
'''

'''
 The idea is to generate a look up for first 256 numbers (one byte)
'''
class Solution:
    def cnt(self, x):
        t = self.table
        return t[(x) & 0xff]+t[(x>>8) & 0xff] + t[(x>>16) & 0xff]+t[(x>>27) & 0xff]

#fill table   #dp
    def __init__(self):
        self.table = {0:0}
        for i in range(1, 256):
            self.table[i] = i&1+self.table[i>>1]