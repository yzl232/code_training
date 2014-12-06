# encoding=utf-8
'''
找钱问题， 不过是简化版的。 就是输入最多是10块钱， 东西最贵是1块钱， 有5
块1块25c 10c 5c和1c的，输出找钱的组合。 不过只要求输出一种，就是有大的用大的
那种。相对就简单很多了。 e.g.  付了10块，东西1c, 找1张5 4张1       3个quarter 2个
dime  4个pennies


The program would take as input the amount the customer
gives and outputs how many 1 cent coins, 5 cent coins, 10 cent coins , 25 cent coins and $1 bill you need to give out.

'''


#这道题目自己写的时候可以多复制粘贴


class Solution:
    def printChange(self, receive, actual):
        change = (receive-actual)*100
        print change/100
        change = change%100
        print change/50
