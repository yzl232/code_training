# encoding=utf-8
'''
#google面经里边有。。擦。。

Binary representation of a given number

Write a program to print Binary representation of a given number.
还是比较巧妙的。
'''
class Solution:
    def binaryF(self, n):
        self.result = []
        self.dfs(n)
        return ''.join(self.result)

    def dfs(self, n):
        if n==0: return
        self.dfs(n/2)
        self.result.append(str(n%2))

s = Solution()
print s.binaryF(5)