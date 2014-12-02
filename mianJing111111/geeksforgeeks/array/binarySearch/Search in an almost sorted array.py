# encoding=utf-8
'''

Search in an almost sorted array

Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient function to search an element in this array. Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1].

For example consider the array {2, 3, 10, 4, 40}, 4 is moved to next position and 10 is moved to previous position.

Example:
# 3和10混淆了， 40和20混淆了。
Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
Output: 2
Output is index of 40 in given array

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 90
Output: -1
-1 is returned to indicate element is not present

'''
class Solution:
    def bs(self, arr, x):
        l=0; h=len(arr)-1
        while l<=h:
            m = l+(h-l)/2
            if x==arr[m]: return m
            elif m>l and arr[m-1]==x: return m-1
            elif m<h and arr[m+1]==x: return m+1        #每次都检查3个点
            elif arr[m]>x:   h =m-2   #比较赞的题目
            else:  l=m+2
