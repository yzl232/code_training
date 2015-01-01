# encoding=utf-8
'''
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

def getDigit(n):
    digits = 0
    minV = None
    maxV = -1
    while True:
        digits += 1
        minV = maxV + 1
        maxV = int('9' * digits)
        size = (maxV - minV + 1) * digits
        if size > n:   break
        n -= size
    number, digit = minV + n / digits, n % digits
    return int(str(number)[digit])

print getDigit(15)


