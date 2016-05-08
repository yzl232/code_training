# encoding=utf-8

'''
打过来电话后人家先让我自我介绍一下，并且给她讲一个project，完后就是google doc做题。
我就只有一道题，是string decompression.
example 
3[ab]2[abc]e 变成 ababababcabce
3[2[de]f] 变成  dedefdedefdedef
'''

#想法。发现一个[,  迅速搜]的位置(cnt==0的方法).       然后recursion.

#然后用recursion
class Solution:
    def solve(self, s):
        return self.dfs(s)


    def dfs(self, s):
        if not s: return ""
        if all("a"<=ch<="z" for ch in s): return s
        if s[0].isdigit():
            pre = i = 0
            while i<len(s) and s[i].isdigit(): i+=1
            cnt = int(s[pre:i]);  j=i
            bracket = 1;  i+=1
            while i<len(s):
                if s[i]=="[": bracket+=1
                elif s[i]=="]": bracket-=1
                if bracket==0: return cnt*(self.dfs(s[j+1:i]))+self.dfs(s[i+1:])
                i+=1
print Solution().solve("3[ab]2[abc]e")
print Solution().solve("3[2[de]f]")