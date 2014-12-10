# encoding=utf-8
'''
Write a method to return first five 10 digit prime numbers
先试试暴力法


这个题目下面有个很好的思路，

任何大于3的素数都可以表示成为6q +/- 1。

证明：

对于任何数n>3

处以6之后能表示成6q+r

r:0,1,2,3,4,5

当r为0,2,4的时候，n可以被2整除，所以不是素数；

当n为3的时候，可以被3整除；

只能为1,5，第一种就是6q+1,第二种是6q+5 = 6(q+1)-1

'''

def specificPrimes():
    primes = [2]
    for i in range(3, 10**5, 2):
        isPrime = True
        for j in primes:
            if j**2 > i:
                break
            elif i % j != 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)

    largePrimes = []
    for i in range(10**9, 10**10):
        rem = i%6
        if rem!=1 or rem!=5: continue
        if len(largePrimes) == 5:
            break
        isPrime = True
        for j in primes:
            if j**2> i:
                break
            elif i % j != 0:
                isPrime = False
                break
        if isPrime:
            largePrimes.append(i)

    return largePrimes

print specificPrimes()


