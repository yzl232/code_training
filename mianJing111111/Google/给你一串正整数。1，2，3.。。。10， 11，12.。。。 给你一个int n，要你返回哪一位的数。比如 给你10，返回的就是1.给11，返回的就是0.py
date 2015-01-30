# encoding=utf-8
# 给你一串正整数。1，2，3.。。。10， 11，12.。。。 给你一个int n，要你返回哪一位的数。比如 给你10，返回的就是1.给11，返回的就是0

#规律。 1*9， 2*90， 3*900， 。。。。。

'''
# encoding=utf-8

Imagine you have a sequence of the form 0123456789101112131415... where each digit is in a position, for example the digit in the position 5 is 5, in the position 13 is 1, in the position 19 is 4, etc.

Write a function that given a position returns the digit in that position.

(You could think that this sequence is an array where each cell only holds one digit so given an index return what digit is in that index, however you cannot really create an array since the sequence is infinite, you need a way to based on the index calculate the digit that goes there).

The function has to return a single digit.

Other examples:

index = 100, result = 5
index = 30, result = 2
index = 31, result = 0
index = 1000, result = 3
'''

# 先是1~9， 10~99， 100~999

# 先是1~9， 10~99， 100~999
# #规律。 1*9， 2*90， 3*900， 。。。。。

def getDigit(n):
    x = 0
    while True:
        x += 1
        size = (10**x-10**(x-1)) * x   #规律。 1*9， 2*90， 3*900， 。。。。。
        if size > n:   break
        n -= size
    number, digit = 10**(x-1) + n / x, n % x
    return int(str(number)[digit])

for i in range(17):
    print getDigit(i)

for i in range(17):
    print getDigit(i)