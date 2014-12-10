# encoding=utf-8

'''
超简洁啊！！！

'''


def ifib(n):
    '''return fibinochi'''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print ifib.__doc__


'''
判断一个数是不是fibonacci

A simple way is to generate Fibonacci numbers until the generated number is greater than or equal to ‘n
'''

class Solution:
    def isFibo(self, x):
        a=0; b = 1
        while a<x:
            a, b =b, a+b
        return a==x

'''
logN 解法。  利用了leetcode的求power部分

使用了matrix得power.
m=
[1 1]
[1 0]

m*m=
[2 1]
[1 1]


m*m*m=
[3 2]
[2 1]


所以不会矩阵乘法，可以简单的两行相加

[Fn+1, Fn]
[Fn, Fn-1]

'''

class Solution2:
    def fib(self, n):
        self.e =  [[1, 1], [1, 0]]
        if n==0: return 0
        result = self.pow(n)
        return result[1][0]


    def pow(self, n):       #n是整数。 可以为负数
        if n<0: return 1.0/self.pow( -n)
        if n == 0:return 1
        if n==1: return self.e
        elif n>1:
            half = self.pow(n/2)
            t = self.multiply(half, half)
            if n%2 == 0 : return t
            else: return self.multiply(t, self.e)

    def multiply(self, f, m):
        x = f[0][0] * m[0][0] + f[0][1] * m[1][0]
        y = f[0][0] * m[0][1] + f[0][1] * m[1][1]
        z =  f[1][0]*m[0][0] + f[1][1]*m[1][0]
        w = f[1][0]*m[0][1] +f[1][1]*m[1][1]
        return [[x, y], [z, w]]
'''
Time Complexity: O(Logn)
Extra Space: O(Logn) if we consider the function call stack size, otherwise O(1).
'''