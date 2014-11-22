# encoding=utf-8
'''
Write a program to generate all prime numbers from 2 to N for any N value
'''

class Solution:
    def primes(self, n):
        return [i for i in range(2, n+1) if self.isprime(i)]

    def isprime(self, n):
        if n==2 or n==3: return True
        if n%2==0:     return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:    return False
        return True
s = Solution()
print s.primes(100)