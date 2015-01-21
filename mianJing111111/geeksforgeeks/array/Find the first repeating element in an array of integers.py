# encoding=utf-8
'''
Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest.

Examples:
本来想用简单的hash。但是不行
比如  3, 5, 5 ,3

这样用hash
We can Use Hashing to solve this in O(n) time on average. The idea is to traverse the given array from right to left and update the minimum index whenever we find an element that has been visited on right side.

必须全部扫完一遍才能知道。

'''
#和2sum一样。 也是先查后存的思想

class Solution:
    def findFirs(self, arr):
        ret = None; d = {}
        for i in range(len(arr)-1, -1, -1):
            if arr[i] in d:  ret = i
            else:  d[arr[i]] = True
        return ret