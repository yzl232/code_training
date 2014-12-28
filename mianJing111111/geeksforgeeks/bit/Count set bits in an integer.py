# encoding=utf-8
'''

Count set bits in an integer

Write an efficient program to count number of 1s in binary representation of an integer.
'''
'''
Count set bits in an integer
'''
#下面这个解法效率更高
class Solution2:
    def cntBits(self, n):
        cnt=0
        while n:
            n&=n-1
            cnt+=1
        return cnt

#也可以查表

#这道题目
#Program to count number of set bits in an (big) array

'''
Given is a 32 bit number...that means a 4 byte integer.
p[0], p[1], p[2], p[3] are the 4 bytes of the integer
so for example:

 v = 10010100100010001011101100111111
the 4 bytes are:
p[0] = 00111111 = 63
p[1] = 10111011 = 187
p[2] = 10001000 = 136
p[3] = 10010100 = 148

so number of bits set in v = number of bits set in p[0] +
							 number of bits set in p[1] +
							 number of bits set in p[2] +
							 number of bits set in p[3]

If BitSetsTable is an array where BitSetsTable[i] = number of set bits in i, then

number of bits set in v = BitSetsTable[p[0]] +
						  BitSetsTable[p[1]] +
						  BitSetsTable[p[2]] +
						  BitSetsTable[p[3]]

Now how to fill up the BitSetsTable:
'''

