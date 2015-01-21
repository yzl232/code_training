# encoding=utf-8
'''

Print all permutations with repetition of characters

Given a string of length n, print all permutation of the given string. Repetition of characters is allowed. Print these permutations in lexicographically sorted order
Examples:

Input: AB
Ouput: All permutations of AB with repetition are:
      AA
      AB
      BA
      BB

Input: ABC
Output: All permutations of ABC with repetition are:
       AAA
       AAB
       AAC
       ABA
       ...
       ...
       CCB
       CCC

稍微变化的dfs
是挺特别

n**n 指数的复杂
'''
#因为candidates不变
class Solution:
    def allPer(self, s):
        self.ret = []; self.n = len(s); self.c = list(s)
        self.dfs( '')
        return self.ret

    def dfs(self, cur):  #还满少见的哈。
        if len(cur)==self.n:
            self.ret.append(cur)
            return
        for ch in self.c:
            self.dfs(cur+ch)
s = Solution()
print s.allPer('AB')
print s.allPer('ABC')