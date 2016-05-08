# encoding=utf-8
'''
Imagine you have a sequence of the form 123456789101112131415... where each digit is in a position, for example the digit in the position 5 is 5, in the position 13 is 1, in the position 19 is 4, etc.

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
    def getSize(i): return (10**i-10**(i-1)) * i
    i = 1
    while getSize(i)<=n:
        n -= getSize(i)
        i += 1       #   9*i*(10**(i-1)) #规律。 1*9， 2*90， 3*900， 。。。。。
    number, digit = 10**(i-1) + n / i, n % i
    return int(str(number)[digit])

for i in range(17):
    print getDigit(i)
'''

def getDigit(n):
    i = 0
    while True:
        i += 1
        size = (10**i-10**(i-1)) * i        #   9*i*(10**(i-1)) #规律。 1*9， 2*90， 3*900， 。。。。。
        if size > n:   break
        n -= size
    number, digit = 10**(i-1) + n / i, n % i
    return int(str(number)[digit])

'''


# Count the number of digits that in all legal positive numbers below N
# 也是G家
def smallerCnt(x):  # x=1005.,  9+2*90+3*900+6*4
    n=len(str(x))
    return sum((10**i-10**(i-1)) * i for i in range(1, n))+(x-10**(n-1))*n
#规律。 1*9， 2*90， 3*900， 。。。。。
print smallerCnt(1005)
print smallerCnt(12)