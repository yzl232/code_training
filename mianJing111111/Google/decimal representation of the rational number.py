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
    # @return a string
    def fractionToDecimal(self, a, b):   #不考虑负号只要9行
        ret = '-' if  a*b<0 else ''  #
        a=abs(a); b=abs(b)
        intP, rem = a / b,  a % b  #real就是 intPart
        ret +=str(intP)
        floatP = ''; i=0; d = {}  #hash是无序的，所以加个有序的decimal
        while rem and rem not in d:   # i记录的是在floatP中的位置。
            d[rem] = i  #先更新hashmap。再乘以10. hashmap存的是循环开始位置
            rem *= 10  #这一步是核心之一。
            x, rem=rem/b, rem%b
            floatP+=str(x); i+=1
        if rem==0:    return ret+'.' + floatP if floatP else ret
        i = d[rem]
        return ret+ '.' +floatP[:i]+ '('+floatP[i:]+')'

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