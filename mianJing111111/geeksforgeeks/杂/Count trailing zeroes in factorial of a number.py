# encoding=utf-8
'''
Given an integer n, write a function that returns count of trailing zeroes in n!.


A trailing zero is always produced by prime factors 2 and 5. I

We can easily observe that the number of 2s in prime factors is always more than or equal to the number of 5s


Trailing 0s in n! = Count of 5s in prime factors of n!
                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
'''
class Solution:
    def findTrailingZeros(self, n):
        count = 0; pow5=5
        while n/pow5>=1:
            count+=n/pow5
            pow5*=5
        return count