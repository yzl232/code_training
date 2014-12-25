# encoding=utf-8
'''
Write a method to determine if two strings are anagrams of each other.
e.g. isAnagram(“secure”, “rescue”) → false
e.g. isAnagram(“conifers”, “fir cones”) → true
e.g. isAnagram(“google”, “facebook”) → false
'''
# O(n)
# 也可以keep an asicii array of 256. 不过一般都可以用hashtable替代。 尽量用hashtable
class Solution:
    def  isAnagram(self, s1, s2):
        d1= self.cnt(s1)
        d2 = self.cnt(s2)
        if len(d1)!=len(d2): return False      #注意检查长度
        for ch in d1:
            if ch not in d2 or d2[ch]!=d1: return False
        return True


    def cnt(self, s):
        d={}
        for ch in s:
            if ch ==' ': continue   #忽略空格
            if ch not in d: d[ch]=0
            d[ch]+=1
        return d