# encoding=utf-8
'''

Count number of binary strings without consecutive 1’s

Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s.

Examples:

Input:  N = 2
Output: 3
// The 3 strings are 00, 01, 10

Input: N = 3
Output: 5
// The 5 strings are 000, 001, 010, 100, 101

2, 3, 5,

I checked it with n=4,the output should be 8
0000,0100,0001,1000,0010,0101,1010,0101

'''
#fibonacci
#虽然是count number。确实没想到dp
#a[i] = a[i - 1] + a[i-2],   a[i-1]代表末尾+0，  a[i-2]代表末尾+1(倒数第二位定为0. 倒数第三位随便)
#1, 1, 2, 3 ,5, 8
class Solution:
    def cntS(self, n):
        if n<1: return
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return b
