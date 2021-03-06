# encoding=utf-8
'''
找出一个数由最少几个平方的和的组成
例子：
input： 14    output:  9 ,4 , 1  虽然也能由1 +1 +....+1组成 但长度是14 不是最优解。。
input:   50     ouput :  25, 25
'''
#G家出现过好几次

#G家题目
#以前的做法是O(n2)。 有更好的O(n1.5)的做法。

class Solution:
    def minNum(self, num):
        dp = [i for i in range(num+1)]
        for i in range(2, num+1):
            dp[i]=min(  1+dp[i-j*j] for j in range(1, int(i**0.5)+1)   )
        return dp[-1]
s = Solution()
print s.minNum(14)
print s.minNum(50)
print s.minNum(12)
print s.minNum(3)


'''
给定一个target number，要求返回一个只由square number（1，4，9，16…）组成的集合，元素的和为target且元素的个数最少。
例子：
14 = 9 + 4 + 1, 12 = 4 + 4 + 4, 10 = 9 + 1
如果返回具体的数， 要怎么做？
'''

#存的是元素。 比较的时候换上len。

class Solution:
    def minNum(self, num):
        dp = [[1]*i for i in range(num+1)]
        for i in range(2, num+1):
            for j in range(1, int(i**0.5)+1):
                if 1+len(dp[i-j*j])<len(dp[i]):
                    dp[i] =dp[i-j*j]+ [j*j]
        return dp[-1]
s = Solution()
print s.minNum(14)
print s.minNum(50)
print s.minNum(12)
print s.minNum(3)


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
# 一个是dp[i-j*j]+1   一个是dp[i-j]*j
