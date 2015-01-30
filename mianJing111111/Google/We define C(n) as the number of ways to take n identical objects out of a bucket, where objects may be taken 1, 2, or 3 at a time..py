# encoding=utf-8
'''
We define C(n) as the number of ways to take n identical objects out of a bucket, where objects may be taken 1, 2, or 3 at a time.

Example: C(4)=7, because you can take 4 objects in the following 7 ways:
1,1,1,1
2,1,1
1,2,1
1,1,2
2,2
3,1
1,3

Write a function for C(n) in the language of your choice.
'''


'''
It's not hard to see that C(n) has the following recursive definition (similar to the Fibonacci numbers):
C(0)=1
C(1)=1
C(2)=2
C(n)=C(n-3)+C(n-2)+C(n-1) (if n>2)

This recursive definition leads to an obvious (and slow) algorithm for computing C(n). Slightly better is:

def C(n):
   L=[1,1,2]
   while n:
       n-=1
       new=L[0]+L[1]+L[2]
       L[0]=L[1]
       L[1]=L[2]
       L[2]=new
   return L[0]

This is okay, but still slow if n is very large. Faster algorithms can be found using linear algebra, similar to fast algorithms for the Fibonacci numbers. One way to regard the previous algorithm is to think of L=[1,1,2] as a vector, and then each iteration replaces L by M*L, where M is the matrix

[0 0 1]
[1 0 1]
[0 1 1]
So what we are really doing is computing the first entry of (M^n)*L. Fast algorithms for matrix exponentiation can accelerate this much faster than just repeatedly multiplying (on the left) by M, n times in a row..
'''

# dp[n] = dp[n-1]+dp[n-2]+dp[n-3]

class Solution:
    def cnt(self, n):
        assert n>0
        a, b, c = 1,2, 4
        for i in range(n-1):
            a, b, c = b, c, a+b+c
        return a
# fibonacci
# logN的方法
'''
x=[1,1,2]

复习一下推导过程。很容易得出
行乘以列
m=
[0 0 1]
[1 0 1]
[0 1 1]
'''