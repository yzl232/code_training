# encoding=utf-8
'''


Compute modulus division by a power-of-2-number

Compute n modulo d without division(/) and modulo(%) operators, where d is a power of 2 number.


'''
class Solution:
    def getMod(self, n, d):
        return n&(d-1)
    
'''
Compute n modulo d without division(/) and modulo(%) operators, where d is a power of 2 number.

Let ith bit from right is set in d. For getting n modulus d, we just need to return 0 to i-1 (from right) bits of n as they are and other bits as 0.

For example if n = 6 (00..110) and d = 4(00..100). Last set bit in d is at position 3 (from right side). So we need to return last two bits of n as they are and other bits as 0, i.e., 00..010. 
'''