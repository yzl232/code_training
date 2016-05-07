# encoding=utf-8
'''
suppose a string is consists of a, b, and c
Now given a integer N, output the amount of all possible strings of length N that don't of have consecutive a,b,c.
e.g. given N=5, string bacca is invalid since the first 3 letters have consecutive a,b,c. and bbbbb is valid.
'''

#这种dp题其实都不大容易。 但是代码都很短。

#O(log n) (arithmetic operations) can be done (view as matrix multiplication).

'''
举出简单例子，可以推导出来
aa_
ab_

f1(n)=f1(n-1)+f2(n-1);
f2(n)=2*f1(n-1)+f2(n-1);
'''

'''
f1(n) is the number of strings with the last two char same;
f2(n) is the number of strings with the last two char different;
f1(n)=f1(n-1)+f2(n-1);
f2(n)=2*f1(n-1)+f2(n-1);
f1(2)=3;
f2(2)=6;
'''
#  a 相同。 b不同。
#

class Solution:
    def solve(self, n):
        if n==1: return 3
        if n==2: return 9
        a, b = 3, 6
        for i in range(n-2):
            a, b = a+b, 2*a+b
        return a+b


'''
class Solution:
    def cnt(self, n):
        if n==1: return 3
        if n==2: return 9
        dp1 = [None for i in range(n+1)]
        dp2 = dp1[:]
        dp1[2]=3;  dp2[2]=6
        for i in range(3, n+1):
            dp1[n] = dp1[n-1]+dp2[n-1]
            dp2[n] = 2*dp1[n-1]+dp2[n-1]
        return dp1[-1]+dp2[-1]

s= Solution()
print s.cnt(3)
'''

