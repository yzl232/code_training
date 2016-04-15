# encoding=utf-8
'''
Write a recursive C function to print reverse of a given string.

Program:
'''
class Solution:
    def reverse(self, s):
        self.ret =''
        def helper(i):
            if i>=len(s): return
            helper(i+1)   #类似stack
            self.ret+=s[i]
        helper(0)
        return self.ret

s = Solution()
print s.reverse('abc')