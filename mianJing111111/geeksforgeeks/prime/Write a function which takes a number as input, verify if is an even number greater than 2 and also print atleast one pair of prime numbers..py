# encoding=utf-8
'''
Write a function which takes a number as input, verify if is an even number greater than 2 and also print atleast one pair of prime numbers.
'''

class Solution:
    def isPrime(self, n):
        if n<=1: return False
        if n==2 or n==3: return True
        if n%2==0: return False
        for i in range(3, int(n**0.5), 2):
            if n%i==0: return False
        return True

    def findPrimePair(self, n):
        if n%2==1: return
        result = []
        for i in range(n/2+1):
            if self.isPrime(i):
                result.append((i, n-i))
        return result