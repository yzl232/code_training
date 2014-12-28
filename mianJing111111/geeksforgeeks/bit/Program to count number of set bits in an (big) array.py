# encoding=utf-8
'''
Program to count number of set bits in an (big) array
'''

'''
 The idea is to generate a look up for first 256 numbers (one byte)
'''
class Solution:
    table = {}
    def cnt(self, x):
        table = self.table
        return table[(x) & 0xff]+table[(x>>8) & 0xff] + table[(x>>16) & 0xff]+table[(x>>27) & 0xff]

#fill table   #dp
    def fill(self):
        for i in range(256):
            self.table[i] = i&1+self.table[i>>1]