# encoding=utf-8
'''
Output top N positive integer in string comparison order. For example, let's say N=1000, then you need to output in string comparison order as below:
1, 10, 100, 1000, 101, 102, ... 109, 11, 110, ...
'''
class Solution:
    def dfs(self,s):
        if int(s)>self.n: return
        self.ret.append(s)
        for i in range(10):  # 0~9都可以
            self.dfs(s+str(i))

    def solve(self, n=1000):
        self.n = n;  self.ret = []
        for i in range(1, 10):  #1~9
            self.dfs(''+str(i))
        return self.ret
s = Solution()
print s.solve(1000)

#感觉很牛逼的样子。 还没有看懂

'''
DFS comes to our rescue.
if you observe a little you can find out that there is a nice pattern
Start with a char 1-9 in that order (9 iterations).
Add a 0-9 to right of string one at a time and recursively do dfs.
if value<=n print it.
recursively keep on adding char to the right.
when value>n. return from dfs call.
'''