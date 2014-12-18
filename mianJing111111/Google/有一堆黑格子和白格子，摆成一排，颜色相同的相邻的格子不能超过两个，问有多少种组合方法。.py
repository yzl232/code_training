# encoding=utf-8
'''
有一堆黑格子和白格子，摆成一排，颜色相同的相邻的格子不能超过两个，问有多少种组合方法。
'''
#让我想起了exclude, include

#典型的dp

'''
dp[i] = dp[i-1]+dp[i-2]  几乎是fibonacci的表达式 。我再想想

 dp[i-1]：x[i]与x[i-1]不同。 比如x[i-1]=0;  +1   与前一位不同
 dp[i-2] : x[i]与x[i-2] 比如 x[i-2]=0;    +11   与前一位相同
'''


#http://codereview.stackexchange.com/questions/63614/count-number-of-ways-to-paint-a-fence-with-n-posts-using-k-colors

def triple_free_combinations(n):
    """Return the number of ways to choose n items , subject to the constraint that no colour appears three
    times in a row.

    """
    if n == 0:     return 1
    a, b = 2, 2 * 2  #初始化
    for i in range(n - 1):
        a, b = b, a + b
    return a

print triple_free_combinations(3)




'''

Count number of binary strings without consecutive 1’s

Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s.

Examples:

Input:  N = 2
Output: 3
// The 3 strings are 00, 01, 10

Input: N = 3
Output: 5
// The 5 strings are 000, 001, 010, 100, 101

2, 3, 5,

I checked it with n=4,the output should be 8
0000,0100,0001,1000,0010,0101,1010,0101

'''
#fibonacci
#虽然是count number。确实没想到dp
#a[i] = a[i - 1] + a[i-2],   a[i-1]代表末尾+0，  a[i-2]代表末尾+01.
#1, 1, 2, 3 ,5, 8
class Solution:
    def cntS(self, n):
        if n<1: return
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return b