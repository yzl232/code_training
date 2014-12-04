# encoding=utf-8
'''
Write a function Add() that returns sum of two integers. The function should not use any of the arithmetic operators (+, ++, –, -, .. etc).

半加器:    00. 01 10 11
&是进位
^是求和
'''
class Solution:  #比较简短。 背下。
    def addBi(self, x, y):
        while y:
            share = x&y  #求进位.  common bits， 左移也是和
            x = x^y  #求和.    求和。   不是common的bits和在x。
            y = share<<1     #common bits和在y
        return x
#

'''
Above is simple Half Adder logic that can be used to add 2 single bits. We can extend this logic for integers. If x and y don’t have set bits at same position(s), then bitwise XOR (^) of x and y gives the sum of x and y. To incorporate common set bits also, bitwise AND (&) is used. Bitwise AND of x and y gives all carry bits. We calculate (x & y) << 1 and add it to x ^ y to get the required result.
'''

s = Solution()
print s.addBi(4, 9)