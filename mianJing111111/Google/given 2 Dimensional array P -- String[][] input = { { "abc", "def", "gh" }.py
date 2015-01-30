# encoding=utf-8
'''
given 2 Dimensional array
I/P -- String[][] input = { { "abc", "def", "gh" },
{ "f", "g" },
{ "qrt","xyz","pqr" } };

Program shd return a 2-D Array with
O/P -- { { "abcfqrt", "abcfxyz", "abcfpqr" ,abcgqrt and so on ..
'''
#明明就是普通的DFS。我居然写不出。..

#如果只有3列
class Solution:
    def combs(self, a, b, c):
        return [x+y+z for x in a for y in b for z in c]

#如果任意列
class Solution:  #用一个坐标表示第几行。
    def combs2(self, arr):
        self.arr = arr
        self.ret=[]
        self.dfs('', 0)
        return self.ret

    def dfs(self, cur, i):
        if i==len(self.arr):
            self.ret.append(cur)
            return
        for x in self.arr[i]:
            self.dfs(cur+x, i+1)

s = Solution()
print s.combs2([[ "abc", "def", "gh"], ["f", "g"], ["qrt","xyz","pqr"]])
