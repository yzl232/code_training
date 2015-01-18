# encoding=utf-8
'''

Find the number of zeroes

Given an array of 1s and 0s which has all 1s first followed by all 0s. Find the number of 0s. Count the number of zeroes in the given array.

Examples:

Input: arr[] = {1, 1, 1, 1, 0, 0}
Output: 2

Input: arr[] = {1, 0, 0, 0, 0}
Output: 4

Input: arr[] = {0, 0, 0}
Output: 3

Input: arr[] = {1, 1, 1, 1}
Output: 0

'''
#又碰到了。。
'''
 Binary Search to find the first occurrence of 0. Once we have index of first element, we can return count as n – index of first zero.
'''

class Solution:
    def isMajority(self, arr):
        r = self.rightS(arr, 1)
        if r==-1: return 0
        return r+1

    def rightS(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==len(arr)-1 or arr[m+1]!=x) and arr[m]==x: return m
            elif arr[m]>x:  h=m-1
            else:   l=m+1    #其他时候，相等的时候，也是在右边
        return -1   #没找到返回一个flag