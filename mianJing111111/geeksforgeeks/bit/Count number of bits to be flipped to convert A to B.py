# encoding=utf-8
'''
Count number of bits to be flipped to convert A to B
'''
class Solution:
    def coutBits(self, n):
        count = 0
        while n:
            count+=n%2   #就是求binary形式那道题      n&1
            n/=2
        return count

    def countFlip(self, a, b):
        return self.coutBits(a^b)
