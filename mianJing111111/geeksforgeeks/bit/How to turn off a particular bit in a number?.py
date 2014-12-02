# encoding=utf-8
'''
Given a number n and a value k, turn of the k’th bit in n.

Examples:

Input:  n = 15, k = 1
Output: 14

Input:  n = 15, k = 2
Output: 13

Input:  n = 15, k = 3
Output: 11

'''
class Solution:
    def turnOff(self, n, k):
        return n&(~(1<<(k-1)))