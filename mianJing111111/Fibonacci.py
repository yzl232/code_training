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
        if a==x: return True
        return False

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


[Fn+1, Fn]
[Fn, Fn-1]

'''

class Solution2:
    def fib(self, n):
        self.x =  [[1, 1], [1, 0]]
        if n==0: return 0
        result = self.pow(n)
        return result[1][0]

    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, n):
        if n == 0:return 1
        elif n==1: return self.x
        elif n>1:
            half = self.pow(n/2)
            square = self.multiply(self.x, self.x)
            if n%2 == 0 : return square
            else: return self.multiply(square, self.x)
        else:
            return 1.0/self.pow(-n)

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