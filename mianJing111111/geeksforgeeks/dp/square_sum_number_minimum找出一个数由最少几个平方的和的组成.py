# encoding=utf-8
'''
找出一个数由最少几个平方的和的组成
例子：
input： 14    output:  9 ,4 , 1  虽然也能由1 +1 +....+1组成 但长度是14 不是最优解
input:   50     ouput :  25, 25
'''
#G家题目
class Solution:
    def minNum(self, num):
        dp = [i for i in range(num+1)]
        for i in range(2, num+1):
            if i== (int(i**0.5))**2:  dp[i] = 1
            else:     dp[i] = min( dp[j]+dp[i-j] for j in range(0, i))
        return dp[-1]
s = Solution()
print s.minNum(14)
print s.minNum(50)