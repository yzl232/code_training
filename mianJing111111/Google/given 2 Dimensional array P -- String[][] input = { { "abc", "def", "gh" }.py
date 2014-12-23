# encoding=utf-8
'''
given 2 Dimensional array
I/P -- String[][] input = { { "abc", "def", "gh" },
{ "f", "g" },
{ "qrt","xyz","pqr" } };

Program shd return a 2-D Array with
O/P -- { { "abcfqrt", "abcfxyz", "abcfpqr" ,abcgqrt and so on ..
'''
#明明就是普通的DFS。我居然写不出。

#如果只有3列
class Solution:
    def combs(self, a, b, c):
        return [x+y+z for x in a for y in b for z in c]

#如果任意列
class Solution:
    def combs2(self, arr):
        self.arr = arr
        self.ret=[]
        self.dfs('', 0)
        return self.ret

    def dfs(self, cur, n):
        if n==len(self.arr):
            self.ret.append(cur)
            return
        for x in self.arr[n]:
            self.dfs(cur+x, n+1)

s = Solution()
print s.combs2([[ "abc", "def", "gh"], ["f", "g"], ["qrt","xyz","pqr"]])
