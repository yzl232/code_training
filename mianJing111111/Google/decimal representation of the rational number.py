# encoding=utf-8
'''

Write a function which, given two integers (a numerator and a denominator), prints the decimal representation of the rational number "numerator/denominator".
Since all rational numbers end with a repeating section, print the repeating section of digits inside parentheses; the decimal printout will be/must be

Example:
1 , 3 = 0.(3)
2 , 4 = 0.5(0)
22, 7 = 3.(142857)

etc..

括号里的是重复循环的部分
'''
#这道题目主要利用了整数mod的思想
#利用了hashmap保存mod的余数remainder
class Solution:
    def divide(self, a, b):
        real, remain = a / b,  a % b
        decimal = []; remainders = {}  #hash是无序的，所以加个有序的decimal
        i = 0
        while remain != 0 and remain not in remainders:
            remainders[remain] = 1
            remain *= 10
            digit, remain=remain/b, remain%b
            decimal.append(str(digit))
        if remain==0: return str(real) + '.' + ''.join(decimal) +  '(0)'
        decimal= ['(']+decimal+[')']
        return str(real) + '.' + ''.join(decimal)

s = Solution()
print  s.divide(1, 3)
print  s.divide(22, 3)
print  s.divide(1, 2)
print  s.divide(39, 37)
print  s.divide(1, 373)
'''
#39/37
remain = 2
remain = 20
remain
当出现重复的remain的时候，循环就开始了。
'''