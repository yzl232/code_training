# encoding=utf-8
'''
Find the Number Occurring Odd Number of Times

只有一个元素出现odd number
Find the Number Occurring Odd Number of Times

Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times. Find the number in O(n) time & constant space.

Example:
I/P = [1, 2, 3, 2, 3, 1, 3]
O/P = 3

简单的想法是hashtable    O(n) space and time
xor是O(n)

'''
class Solution:
    def findOnlyNumOdd(self, arr):
        s = 0
        for i in arr:
            s ^=i
        return s
s = Solution()
print s.findNumOdd([1, 2, 3, 2, 3, 1, 3])


