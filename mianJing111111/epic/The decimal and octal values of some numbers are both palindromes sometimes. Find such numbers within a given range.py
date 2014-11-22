# encoding=utf-8
'''
The decimal and octal values of some numbers are both palindromes sometimes. Find such numbers within a given range

'''
class Solution:
    def isPalindrom(self, s):
        i =0;  j = len(s)-1
        while i<j:
            if s[i]!=s[j]: return False
            i+=1; j-=1
        return True

    def decimalToOctal(self, decimal):
        s = ''
        while decimal!=0:
            remainder = decimal%8
            decimal = decimal/8
            s = str(remainder)+s
        return s

    def getPanlindrom(self, bound):
        result = []
        for i in range(bound):
            if self.isPalindrom(str(i)) and self.isPalindrom(self.decimalToOctal(i)):
                result.append(i)
        return result