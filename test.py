# encoding=utf-8
'''

Write a function which, given two integers (a numerator and a denominator), prints the decimal representation of the rational number "numerator/denominator".
Since all rational numbers end with a repeating section, print the repeating section of digits inside parentheses; the decimal printout will be/must be

Example:
1 , 3 = 0.(3)
2 , 4 = 0.5(0)
22, 7 = 3.(142857)

etc..


39/37 ==>
 39=>20=>200=>150=>

括号里的是重复循环的部分
'''
#这道题目主要利用了整数mod的思想
#利用了hashmap保存mod的余数remainder
class Solution:
    def divide(self, a, b):   #才8行！ 帅
        real, remain = a/b, a%b
        decimal = '';  d = {}
        while remain and remain not in d:
            d[remain] = 1
            remain*=10
            decimal+=str(remain/b)
            remain = remain%b
        if not remain: return str(real)+'.'+decimal+'(0)'
        return str(real)+'.'+'('+decimal+')'


s = Solution()

print  s.divide(39, 37)
'''
#39/37
remain = 2
remain = 20
remain
当出现重复的remain的时候，循环就开始了。
'''