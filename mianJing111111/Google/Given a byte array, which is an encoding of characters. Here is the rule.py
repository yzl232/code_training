# encoding=utf-8
'''

Given a byte array, which is an encoding of characters. Here is the rule:
    a. If the first bit of a byte is 0, that byte stands for a one-byte
character
    b. If the first bit of a byte is 1, that byte and its following byte
together stand for a two-byte character

Now implement a function to decide if the last character is a one-byte
character or a two-byte character

Constraint: You must scan the byte array from the end to the start.
Otherwise it will be very trivial.





本题的关键就是从后往前看到第一个0开始的点是个断点.
无论那个0开头自己解释自己还是跟它前面的那个走,(不可能跟后面走)

都不影响0开头的后面的那个是个起始字节这个结论.
所以就变成了奇偶问题了.

'''
#比如所有char都是1开头。 那么非常难以判断。
#  01110
#11110
class Solution:
    def firstBit(self):
        pass

    def odd(self, arr):
        n = len(arr)
        if self.firstBit(arr[-1])==1:  return '2-byte'
        for i in range(n-2, -1, -1):
            if self.firstBit(arr[i])==0:   break
        if (n-1-i)%2==1: return '1 byte'
        return '2-byte'