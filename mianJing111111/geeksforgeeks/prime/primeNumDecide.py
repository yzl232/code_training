# encoding=utf-8

# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
'''
素数的题目。考虑到1， 2， 3~根号n的奇数就可以了。

是素数，则只有本身一个prime factor
如果不是prime,   则至少有2个prime factors
则2个factors， 如果都大于n**2， 不可能。 所以至少一个小于n**2


If an integer has two prime factors, then at least one of them does not exceed the square root of the integer. So the answer to your question is "No."

证明
Every composite number has at least one prime factor less than or equal to square root of itself.
This property can be proved using counter statement. Let a and b be two factors of n such that a*b = n. If both are greater than \sqrt{n}, then a.b > \sqrt{n} * \sqrt{n} which contradicts the expression “a * b = n”.

In step 2 of the above algorithm, we run a loop and do following in loop
a) Find the least prime factor i (must be less than \sqrt{n})
b) Remove all occurrences i from n by repeatedly dividing n by i.
c) Repeat steps a and b for divided n and i = i + 2. The steps a and b are repeated till n becomes either 1 or a prime number.

'''


def isprime(n):
    if n<=1: return False
    if n==2 or n==3: return True
    if n%2==0:     return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:    return False
    return True

# test ...
print isprime(1)       # False
print isprime(2)       # True
print isprime(3)       # True
print isprime(29)      # True
print isprime(345)     # False
print isprime(999979)  # True
print isprime(999981)  # False

# extra test ...
print isprime(49)      # False
print isprime(95)      # False