# encoding=utf-8
'''

Check if a given string is a rotation of a palindrome



其实和这道题目类似，
A Program to check if strings are rotations of each other or not

Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1 using only one call to strstr routine?
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

s = S1+S2
check if

'''
# s1, s2实际上是对称的。
class Solution:
    def isRotate(self, s1, s2):
        return s2 in (s1+s1)
    pass