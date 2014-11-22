# encoding=utf-8
'''
Write a program to add one to a given number. You are not allowed to use operators like ‘+’, ‘-‘, ‘*’, ‘/’, ‘++’, ‘–‘ …etc.

Examples:
Input: 12
Output: 13

Input: 6
Output: 7

楼主先用leetcode。 完全解法。  然后套上条件。用了hashmap。 套用
'''

class Solution:
    def addOne(self, n):
        return -(~n)

s = Solution()
print s.addOne(5)
print s.addOne(-5)