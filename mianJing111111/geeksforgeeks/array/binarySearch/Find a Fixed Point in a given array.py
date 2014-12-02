# encoding=utf-8
'''

Find a Fixed Point in a given array

Given an array of n distinct integers sorted in ascending order, write a function that returns a Fixed Point in the array, if there is any Fixed Point present in array, else returns -1. Fixed Point in an array is an index i such that arr[i] is equal to i. Note that integers in array can be negative.

Examples:

  Input: arr[] = {-10, -5, 0, 3, 7}
  Output: 3  // arr[3] == 3

  Input: arr[] = {0, 2, 5, 8, 17}
  Output: 0  // arr[0] == 0


  Input: arr[] = {-10, -5, 3, 4, 7, 9}
  Output: -1  // No Fixed Point

'''
#是sorted array,  搜索用binary search
class Solution:
    def bs(self, arr):
        l = 0; h = len(arr)-1
        while l<=h:
            m = l+(h-l)/2
            if arr[m]==m: return m
            elif arr[m]>m:  h = m-1
            else:  l = m+1
        return