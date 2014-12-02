# encoding=utf-8
'''


Compute modulus division by a power-of-2-number

Compute n modulo d without division(/) and modulo(%) operators, where d is a power of 2 number.


'''
class Solution:
    def getMod(self, n, d):
        return n&(d-1)