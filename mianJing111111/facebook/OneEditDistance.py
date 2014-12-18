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
#aa,  aab
#aba  aaa
#aa,   baa
#总共就差1和长度相等2种情况。  长度相等很好解决。  差一也好解决。
#差1得两种情况:在末尾。 在前面或者中间。
class Solution: #关键就是背下后面4行
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):  #背下就好
        m=len(s); n=len(t)  #保持n比较大
        if m>n: return self.isOneEditDistance(t, s)
        if n-m>1: return False
        i=0; dif = n-m
        while i<m and s[i]==t[i]: i+=1
        if i==m: return dif==1     #aaa,   aaab这种情况
        if dif==0: i+=1    #替换,跳过  diff==1不能跳过。 要检查 #aa,   aba
        while i<m and s[i]==t[i+dif]: i+=1
        return i==m