# encoding=utf-8
'''
Find the smallest number whose digits multiply to a given number n

Given a number ‘n’, find the smallest number ‘p’ such that if we multiply all digits of ‘p’, we get ‘n’. The result ‘p’ should have minimum two digits.

Examples:

Input:  n = 36
Output: p = 49
// Note that 4*9 = 36 and 49 is the smallest such number

Input:  n = 100
Output: p = 455
// Note that 4*5*5 = 100 and 455 is the smallest such number

Input: n = 1
Output:p = 11
// Note that 1*1 = 1

Input: n = 13
Output: Not Possible


Case 1: n < 10 When n is smaller than n, the output is always n+10. For example for n = 7, output is 17. For n = 9, output is 19.

Case 2: n >= 10 Find all factors of n which are between 2 and 9 (both inclusive). The idea is to start searching from 9 so that the number of digits in result are minimized. For example 9 is preferred over 33 and 8 is preferred over 24.
Store all found factors in an array. The array would contain digits in non-increasing order, so finally print the array in reverse order.


比暴力法要快很多直接从因子， factor入手。

贪心法：    从9开始，尝试是不是factor
9~2.  这样子
'''
class Solution:
    def finsSmallest(self, n):
        if n<10: return n+10    #题目的意思看来是最少两位数
        ret = []
        for i in range(9, 1, -1):
            while n%i==0:
                n/=i
                ret.append(str(i))
        return "".join(ret[::-1]) if n==1 else None
s = Solution()
print s.finsSmallest(3)
print s.finsSmallest(100)
print s.finsSmallest(26)