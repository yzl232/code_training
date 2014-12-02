# encoding=utf-8
'''
Print squares of first n natural numbers without using *, / and -

Given a natural number ‘n’, print squares of first n natural numbers without using *, / and -.

Input:  n = 5
Output: 0 1 4 9 16

Input:  n = 6
Output: 0 1 4 9 16 25


We strongly recommend to minimize the browser and try this yourself first.

Method 1: The idea is to calculate next square using previous square value. Consider the following relation between square of x and (x-1). We know square of (x-1) is (x-1)2 – 2*x + 1. We can write x2 as

x2 = (x-1)2 + 2*x - 1     如果能用减法的话，直接用2*x-1
x2 = (x-1)2 + x + (x - 1)
'''
class Solution:
    def printSquare(self, n):
        square = 0; prev = 0
        for i in range(n):
            square = square+i+prev
            prev = i
            print square

s = Solution()
print s.printSquare(12)