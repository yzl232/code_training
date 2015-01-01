# encoding=utf-8
'''
八进制的plus one
'''
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            s = digits[i] + carry
            digits[i], carry = s%8, s/8  #10改成8而已。。。。好单纯
        if carry:    digits = [1] + digits
        return digits