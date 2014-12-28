# encoding=utf-8
'''
write the most efficient (in terms of time complexity) function getNumberOfPrimes which takes in an integer N as its parameter.

to return the number of prime numbers that are less than N

Sample Testcases:
Input #00:
100
Output #00:
25

Input #01:
1000000
Output #01:
78498
'''




class Solution:
    def sieve(self,n):
        noprimes = set()
        ret = []
        for i in range(2, n+1):
            if i not in noprimes:
                ret.append(i)
                noprimes.update(range(i*i, n+1, i))   #对素数，追加 no primes
        return ret