# encoding=utf-8
'''
使用递归实现
Implement strstr() to Find a Substring in a String

'''


class Solution:
    def strstr(self, s1, s2):
        if not s2: return s1  #非空就是找到了
        if not s1:  return
        if s1[0]==s2[0] and self.strstr(s1[1:], s2[1:]): return s1
        return self.strstr(s1[1:], s2)

'''


class Solution:
    def strstr(self, s1, s2):
        if not s2: return ''  #非空就是找到了
        if not s1:  return None
        if s1[0]==s2[0] and self.strstr(s1[1:], s2[1:]): return s1
        return self.strstr(s1[1:], s2)
'''
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, s, s1):
        for i in range(len(s)-len(s1)+1):  #举例。   n1=n2=1,
            if s[i:i+len(s1)] == s1: return i
        return -1

