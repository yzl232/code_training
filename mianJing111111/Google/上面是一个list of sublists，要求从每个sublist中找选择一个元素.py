# encoding=utf-8
'''
1. 【【2，3，4】【1】【6，7】】
上面是一个list of sublists，要求从每个sublist中找选择一个元素，输出所有可能，比如
【2，1，6】，【2，1，7】，【3，1，6】。。。
follow up：如果其中有的sublist是空，如何解决，我回答说需要先定义这种情况下的输出才能确定怎么修改
【【2，3，4】，【】，【6，7】】，那么会输出
【2，6】，【2，7】，【3，6】。。。也就是如果非空，那么必须选一个，如果空，那么就跳过
'''

# 出现过两次
# encoding=utf-8
'''
given 2 Dimensional array
I/P -- String[][] input = { { "abc", "def", "gh" },
{ "f", "g" },
{ "qrt","xyz","pqr" } };

Program shd return a 2-D Array with
O/P -- { { "abcfqrt", "abcfxyz", "abcfpqr" ,abcgqrt and so on ..
'''
#如果只有3列
class Solution5:
    def combs(self, a, b, c):
        return [x+y+z for x in a for y in b for z in c]

#如果任意列
class Solution:
    def combs2(self, arr):   #做法。 递归的时候。 每一层递归是arr[row]
        self.arr = arr
        self.ret=[]
        self.dfs('', 0)
        return self.ret

    def dfs(self, cur, row):
        if row==len(self.arr):
            self.ret.append(cur)
            return
        for x in self.arr[row]:
            self.dfs(cur+x, row+1)

s = Solution()
print s.combs2([[ "abc", "def", "gh"], ["f", "g"], ["qrt","xyz","pqr"]])
