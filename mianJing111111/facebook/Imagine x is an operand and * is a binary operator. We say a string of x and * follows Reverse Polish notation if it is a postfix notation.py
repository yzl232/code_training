# encoding=utf-8
'''
Imagine x is an operand and * is a binary operator. We say a string of x and * follows Reverse Polish notation if it is a postfix notation.

For example strings xx*, x, and xx*xx** follow Reverse Polish notation.

Given a string of x and *, how many insert, delete, and replace operations are needed to make the string follow the RPN.

For example, xx* need 0 operation to follow RPN since it already follows RPN.
x*x needs two operations to become xx* which follows RPN.
*xx* needs one operation to become xx* which follows RPN.

Your algorithm should work for a string of size up to 100.

Sample Input:

5
x
xx*
xxx**
*xx
xx*xx**

Sample Output:

0
0
0
2
0

Explanation:

For the first three cases, the input expression is already a valid RPN, so the answer is 0. For the fourth case, we can perform one delete, and one insert operation: xx -> xx -> xx

解法


艹。 怎么这么难。。

One of my friends helped me to solve this problem. The idea is dynamic programming!

Step A: for having RPN, it is enough to have (RPN)(RPN)*, so find the best K where (0,1,...K),(K+1,....,N-1)* is RPN (N is the length of the string).

If the last character is x, you can delete it and find the best answer for (0,....,N-1)
or replace it with an asterisk and go to Step A,
or add an asterisk to the end and find the best K where (1,0,...K),(K+1,....N)* is RPN.

插入*和删除x是等效的。  只考虑删除就好
#不用深入理解。 背下就好。
'''
class Solution:
    def getMinEdit(self, s):
        n = len(s)
        dp = [[0 for i in range(n+1)]for j in range(n+1)]
        for i in range(n):
            dp[i][i+1] = 0 if s[i] == 'x' else 1
        for i in range(n-1):
            tmp = s[i:i+2]
            if tmp=='xx': dp[i][i+2] =1   #exclusive
            elif tmp == 'x*': dp[i][i+2] =1
            elif tmp =='**':dp[i][i+2] = 2
            elif tmp == '*x':dp[i][i+2] = 1
#
        for length in range(3, n+1):
            for start in range(n+1-length):
                end = start+length  #exclusive
                if s[end-1] =='*':  #不用改。 直接找
                    dp[start][end] = min ( dp[start][ start+k]+dp[start+k][end-1] for k in range(1, length-1) )  #当k==0就是删除了。
                elif s[end-1] == 'x':
                    dp[start][end] =min ( dp[start][ start+k]+dp[start+k][end-1]+1 for k in range(length-1) )  #replace
        return dp[0][-1]  #delete x in the end, 插入*和删除x是等效的。  只考虑删除就好

#O(n cube)
s = Solution()
print s.getMinEdit("*x*")
print s.getMinEdit("xxx**")
print s.getMinEdit("xx*xx**")
print s.getMinEdit('x')
print s.getMinEdit('*xx')
print s.getMinEdit('**xx')
print s.getMinEdit('x*xxx')
print s.getMinEdit('*x**x*xx**x***xx*xx**x***xxxxxxxx**xxxxxxx*xx****xxx*x***x**x*******xx**x*xx**x*xx***xx**xx*xxxx')