# encoding=utf-8
'''
如果是找2个，或者3个。都是类似解法。

Write an efficient C program to find smallest and second smallest element in an array.

Difficulty Level: Rookie

Algorithm:

1) Initialize both first and second smallest as INT_MAX
   first = second = INT_MAX
2) Loop through all the elements.
   a) If the current element is smaller than first, then update first
       and second.
   b) Else if the current element is smaller than second then update
    second
'''
class Solution:
    def print2Smallest(self, arr):
        n =len(arr)
        if n<2: return
        first=second =  float('inf')
        for i in range(n):
            if arr[i] <= first:   second, first = first, arr[i]
            elif arr[i]<second:    second = arr[i]
        if second==10**10: print 'only one element'
        print first, second