# encoding=utf-8
'''


Find duplicates in O(n) time and O(1) extra space

Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.

For example, let n be 7 and array be {1, 2, 3, 1, 3, 6, 6}, the answer should be 1, 3 and 6.

#
Use array elements as index

'''

#Find the two repeating elements in a given array
#不适合负数。 适合发现repeat  。  而且可以发现任何repeat
class Solution:
    def findRep(self, arr):
        for i in range(len(arr)):
            t = abs(arr[i])
            if arr[t]<0:   print t   #注意是print t.  t重复了。
            else: arr[t]=-arr[t]