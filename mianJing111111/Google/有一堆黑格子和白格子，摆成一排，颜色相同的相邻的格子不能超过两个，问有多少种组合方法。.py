# encoding=utf-8
'''
有一堆黑格子和白格子，摆成一排，颜色相同的相邻的格子不能超过两个，问有多少种组合方法。
'''
#让我想起了exclude, include

#典型的dp

'''
dp[i] = dp[i-1]+dp[i-2]  几乎是fibonacci的表达式 。我再想想

 dp[i-1]：x[i]与x[i-1]不同。    与前一位不同
 dp[i-2] : x[i]与x[i-1]相同, 但与x[i-2]不同   比如    与前一位相同
'''
#  00
#  10


def triple_free_combinations(n):
    """Return the number of ways to choose n items , subject to the constraint that no colour appears three
    times in a row.    """
    if n == 0:     return 1
    a, b = 2, 2 * 2  #初始化
    for i in range(n - 1):
        a, b = b, a + b
    return a






'''
 你可以把黑是0，白是1，然后考考虑二维的，f(i,00/01/10/11)
f(i,00)=f(i-1,10)
f(i,01)=f(i-1,10)+f(i-1,00)
f(i,10)=f(i-1,01)+f(i-1,11)
f(i,11)=f(i-1,01)

然后再精简下，就是把状态00和11合并为same，把状态01和10全并为differ，
same【i】 = differ[i-1];
differ【i】 = same[i-1] + differ[i-1];



#这种题目都是相同与不相同，两种情况


#http://codereview.stackexchange.com/questions/63614/count-number-of-ways-to-paint-a-fence-with-n-posts-using-k-colors
#a表示相同
#b表示不同
def triple_free_combinations(n):
    if n == 1:     return 1
    if n==2: return 4
    same, dif = 2, 2 * 2  #初始化
    for i in range(n - 2):
        same, dif = dif, same + dif  #fibo
    return same

print triple_free_combinations(3)

'''


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

