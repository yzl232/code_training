# encoding=utf-8
'''
Write a program to add one to a given number. You are not allowed to use operators like ‘+’, ‘-‘, ‘*’, ‘/’, ‘++’, ‘–‘ …etc.

Examples:
Input: 12
Output: 13

Input: 6
Output: 7

楼主先用leetcode。 完全解法。  然后套上条件。用了hashmap。 套用
'''
# complement 补码
# 负数为何是正数的取反加1?
#  ~a+1  = -a   不懂。 背吧。 ~a+1  = -a

class Solution:
    def addOne(self, n):
        return -(~n)

s = Solution()
print s.addOne(5)
print s.addOne(-5)


class Operations:
    def addOne(self, a):
        return -(~a)

    def negate(self, a):
        return ~a+1  #吊炸天

    def minus(self, a, b):
        return a +self.negate(b)

    def abs(self, a):
        if a<0: return self.negate(a)
        return a