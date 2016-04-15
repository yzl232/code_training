# encoding=utf-8
'''
Find the minimum distance between two numbers

Given an unsorted array arr[] and two numbers x and y, find the minimum distance between x and y in arr[]. The array might also contain duplicates. You may assume that both x and y are different and present in arr[].

Examples:
Input: arr[] = {1, 2}, x = 1, y = 2
Output: Minimum distance between 1 and 2 is 1.

Input: arr[] = {3, 4, 5}, x = 3, y = 5
Output: Minimum distance between 3 and 5 is 2.

Input: arr[] = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3}, x = 3, y = 6
Output: Minimum distance between 3 and 6 is 4.

Input: arr[] = {2, 5, 3, 5, 4, 4, 2, 3}, x = 3, y = 2
Output: Minimum distance between 3 and 2 is 1.
'''

# leetcode   Shortest Word Distance
class Solution:
    def findMinD(self, arr, x, y):
        n = len(arr); ret = n+1;  prev = -1  #巧妙，只用了一个prev
        for i in range(n):
            if arr[i]==x or arr[i]==y:
                if prev!=-1 and arr[prev]!=arr[i]:  ret = min(ret, i-prev)
                prev =i
        return ret if ret!=n+1 else None