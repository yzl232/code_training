# encoding=utf-8
'''
Given - a number (n) and a sorted array
Find a number in the array having least difference with the given number (n).
'''
class Solution:
    def bs(self, a, target):
        l =0;  h=len(a)-1
        while l<=h:
            m =  l+(h-l)/2
            if target == a[m]:     return m
            elif target > a[m]:   l = m+1
            else:     h = m-1
        return a[l] if abs(a[l]-target)<abs(a[h]-target) else a[h]