# encoding=utf-8
'''
Write a recursive C function to print reverse of a given string.

Program:
'''
class Solution:
    def reverse(self, s):
        self.ret =''
        self.help(s)
        return self.ret

    def help(self, s):
        if not s: return
        self.help(s[1:])   #类似stack
        self.ret+=s[0]

s = Solution()
print s.reverse('abc')