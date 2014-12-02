# encoding=utf-8
'''
/**
* Implement a function OneEditApart with the following signature:
* bool OneEditApart(string s1, string s2)
*
* OneEditApart("cat", "dog") = false
* OneEditApart("cat", "cats") = true
* OneEditApart("cat", "cut") = true
* OneEditApart("cat", "cast") = true
* OneEditApart("cat", "at") = true
* OneEditApart("cat", "acts") = false
* Edit is: insertion, removal, replacement
*/
'''
#总共就差1和长度相等2种情况。  长度相等很好解决。  差一也好解决。

#背它的答案。 我的答案始终通不过。
#艹。 leetcode要求  one pass,  in place
class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):  #背下就好
        m=len(s); n=len(t)  #保持n比较大
        if m>n: return self.isOneEditDistance(t, s)
        if n-m>1: return False
        i=0; shift = n-m
        while i<m and s[i]==t[i]: i+=1
        if i==m: return shift==1     #aaa,   aaab这种情况
        if shift==0: i+=1    #替换,跳过
        while i<m and s[i]==t[i+shift]: i+=1
        return i==m






'''





        else:
            for i in range(len(big)):
                if big[i] == small[i]: continue
                else:
                    if small == big[:i]+big[i+1:]: return True
                    return False
'''

class Solution58:
    def isOneEditDistance(self, a, b):
        small = a;  big = b
        if len(small)>len(big):   return self.isOneEditDistance(b, a)
        operations = 0
        if len(big) - len(small)>1: return False
        elif len(big) == len(small): #长度相等。
            for i in range(len(small)):
                if big[i] != small[i]:
                    if operations >0: return False
                    operations+=1
        else:  #长度不等
            for i in range(len(small)):
                if small[i] != big[i+operations]:
                    if operations >0: return False
                    operations+=1
        return True
s = Solution58()
print s.isOneEditDistance('a', '')