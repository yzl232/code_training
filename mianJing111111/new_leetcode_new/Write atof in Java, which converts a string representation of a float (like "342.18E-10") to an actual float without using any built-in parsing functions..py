# encoding=utf-8
'''
Write atof in Java, which converts a string representation of a float (like "342.18E-10") to an actual float without using any built-in parsing functions.


# 和leetcode的atoi超级像啊。


1. detect delimiter "e" and split to left and right parts
2. then two parts are parsed as
* detect the starting character with "+"/"-"
* call atoi() on the right part
* detect delimiter "." on the left part and split into two sections
* use atoi() on two sections
* the 2nd section times power(10, - 2ndSection.size());
* Then combine them together including the sign.

第一次以'e'分裂
第二次以'.'分裂

342.18E-10

'''
class Solution:
    def atof(self, s):
        s=s.lower(); s_exp= s_float = ""
        if 'e' in s:
            i=s.index('e')
            s, s_exp=s[:i], s[i+1:]
        if '.' in s:
            i=s.index('.')
            s, s_float=s[:i], s[i+1:]
        return (self.atoi(s)+self.atoi(s_float)*(0.1)**len(s_float)  )* (10**self.atoi(s_exp))  # 很容易忘记 (0.1)**len(s2)

    # @return an integer
    def atoi(self, s):
        s+='#';  i=0; result =0    # 不用考虑边界'#'
        while s[i]==' ': i+=1  #s[i]=='',   i+=1 这样子用pointer也很好。
        sign = 1
        if s[i]=='+':
            i+=1
        elif s[i]=='-':
            sign = -1
            i+=1
        while '0'<=s[i]<='9':
            result =result*10 + ord(s[i])-ord('0')
            i+=1
        return max(min(result*sign, 2147483647 ), -2147483648)
s = Solution()
print s.atof("342.18E-5")