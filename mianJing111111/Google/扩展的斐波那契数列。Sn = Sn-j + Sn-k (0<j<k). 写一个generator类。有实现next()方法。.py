# encoding=utf-8
# 题目一：扩展的斐波那契数列。Sn = Sn-j + Sn-k (0<j<k). 写一个generator类。有实现next()方法。
class Fibonacci(object):
    def __init__(self, j, k, arr):
        self.j = j
        self.k = k
        self.dp = arr

    def next(self):
        res = self.dp[- self.j] +   self.dp[- self.k]
        self.dp.append(res)
        return res