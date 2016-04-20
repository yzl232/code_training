
# encoding=utf-8
'''
#google面经里边有。。擦。。

Binary representation of a given number

Write a program to print Binary representation of a given number.
还是比较巧妙的。
'''
'''
class Solution:
    def binaryF(self, n):
        self.ret = []
        self.dfs(n)
        return ''.join(self.ret)

    def dfs(self, n):
        if n==0: return
        self.dfs(n>>1)  #还是用位移容易理解。 先搞高位的。
        self.ret.append(str(n&1))
'''
class Solution2:
    def binaryF(self, n):
        ret = ""
        while n:
            ret+=str(n&1)
            n = n>>1
        return ret[::-1]  #逆转
s = Solution2()
print s.binaryF(19)