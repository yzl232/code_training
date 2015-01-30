# encoding=utf-8
'''
Print all interleavings of given two strings



Print all interleavings of given two strings

Given two strings str1 and str2, write a function that prints all interleavings of the given two strings. You may assume that all characters in both strings are different

Example:

Input: str1 = "AB",  str2 = "CD"
Output:
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB

Input: str1 = "AB",  str2 = "C"
Output:
    ABC
    ACB
    CAB


leetcode的变体题目
肯定是递归
另外跟
'''
class Solution:
    def interLeave(self, s1, s2):
        self.ret = []
        self.dfs(s1, s2, '')
        return self.ret

    def dfs(self, s1, s2, cur):
        if not s1 and not s2:
            self.ret.append(cur)
            return
        if s1: self.dfs(s1[1:], s2, cur+s1[0])
        if s2: self.dfs(s1, s2[1:], cur+s2[0])

s = Solution()
print s.interLeave('AB', 'C')
print s.interLeave('AB', 'CD')