# encoding=utf-8
'''
Count number of bits to be flipped to convert A to B
'''

class Solution:
    def cntBits(self, n):
        cnt = 0
        while n:
            cnt+=n&1
            n>>=1
        return cnt

    def countFlip(self, a, b):
        return self.cntBits(a^b)
        
'''   
# Turn off the rightmost set bit

class Solution:
    def cntBits(self, n):
        cnt=0
        while n:
            n&=n-1
            cnt+=1
        return cnt

    def countFlip(self, a, b):
        return self.cntBits(a^b)


Solution:

  1. Calculate XOR of A and B.
        a_xor_b = A ^ B
  2. Count the set bits in the above calculated XOR result.
        countSetBits(a_xor_b)

'''