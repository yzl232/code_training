# encoding=utf-8
'''
一个数，比如7可以拆成 1+3+3 或者3+4。 求拆成的因子相乘积最大的那个
值。 我先给了个 recursion的solution， 每次从1开始拆。 他说不够有效，然后我又
改成dp，用了10分钟，刚好到45分钟，面试结束。
'''
class Solution:
    def solve(self, n):
        dp = [i for i in range(n+1)]     #初始值为不拆分
        for i in range(1, n+1):
            dp[i] = max( [j*dp[i-j]    for j in range(1, i)] +[i])  #注意对称性
        return dp[-1]

#有点像  找出一个数由最少几个平方的和的组成
s= Solution()
print s.solve(7)