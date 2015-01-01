# encoding=utf-8
'''
使用递归实现
Implement strstr() to Find a Substring in a String

'''
class Solution:
    def strstr(self, s1, s2):
        if not s2: return ''  #非空就是找到了
        if not s1:  return None
        if s1[0]==s2[0] and self.strstr(s1[1:], s2[1:]): return s1
        return self.strstr(s1[1:], s2)