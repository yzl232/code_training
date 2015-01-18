# encoding=utf-8
'''

Check for Majority Element in a sorted array

Question: Write a C function to find if a given integer x appears more than n/2 times in a sorted array of n integers.

Basically, we need to write a function say isMajority() that takes an array (arr[] ), array’s size (n) and a number to be searched (x) as parameters and returns true if x is a majority element (present more than n/2 times).


sorted显然用binary search
'''
class Solution:
    def isMajority(self, arr, x):
        n = len(x)
        i = self.bs(arr, x)
        if i==-1: return False
        end = i+n/2
        if end<=n-1 and arr[end]==x: return True
        return False

    def bs(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==0 or arr[m-1]!=x) and arr[m]==x: return m
            elif arr[m]<x: l = m+1
            else:  h=m-1    #其他时候，相等的时候，也是在左边
        return -1