# encoding=utf-8
'''
Write a recursive C function to print reverse of a given string.

Program:
'''
class Solution:
    def reverse(self, s):
        self.result =''
        self.recur(s)
        return self.result

    def recur(self, s):
        if not s: return
        self.recur(s[1:])
        self.result+=s[0]

s = Solution()
print s.reverse('abc')