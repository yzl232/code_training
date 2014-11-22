# encoding=utf-8
'''
// cat, actor -> T
// car, actor -> F

bool anaStrStr (string needle, string haystack)
{
}

Write a function that takes 2 strings , search returns true if any anagram of string1(needle) is present in string2(haystack)


我想到的解法。是建立一个hashMap . 然后把所有的permutation 存进去。 O(n!)+O(m)

用素数是更好的方法:  O(m)

'''

class Solution:
    def isprime(n):
        if n<=1: return False
        if n==2 or n==3: return True
        if n%2==0:     return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:    return False
        return True

    def prime26(self):
        arr = [2, 3, 5, 7]
        for i in range(11, 1000):
            if len(arr)>=26: break
            if self.isprime(i): arr.append(i)
        return arr

    def anaStrStr(self, s1, s2):
        n = len(s1) ;  m=len(s2)
        arr =self.prime26()
        d = {chr(ord('a')+i):arr[i] for i in range(26) }
        product = self.product(s1, d)
        if n>m: return False
        for i in range(m-n):
            tmp = s2[i:i+n]
            if self.product(tmp, d)==product: return True
        return False

    def product(self, s, d):
        ret = 1
        for ch in s:
            ret*=d[ch]
        return ret