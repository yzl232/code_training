# encoding=utf-8
'''
A string 'aBlY' is said to be well ordered because the letters of the string occur one after the other in the alphabet. Write a function where the number of letters in the string are passes as parameter and all such well ordered strings are found.

黑客密码，给你密码长度，让你给出所有可能的密码，要well-ordered，aBk, air这种，大小写都要输出
A string "aBIY" is said to be a well-ordered word as each of the letters are in sequential manner regardless of case. So, "AbLe" is not a well-ordered word.
You are a anti-hacker. you have a number of character sequences. Your task is to generate all possible well-ordered word
'''
# 因为无视大小写。 所以每个subset再找到大小写任意的部分.   就是[1111]  bin(0~2^n-1)  然后map一下就好
class Solution:
    def allGen(self, n):
        candidates = [chr(i+ord('a')) for i in range(26)]
        self.results = []; self.n = n
        self.dfs('', candidates)
        return self.results

    def dfs(self, tmpResult, candidates):
        if len(tmpResult)==self.n:
            self.results.append(tmpResult)
            return
        else:
            for i in range(len(candidates)):
                self.dfs(tmpResult+candidates[i], candidates[i+1:])
s = Solution()
print s.allGen(1)
print s.allGen(2)

