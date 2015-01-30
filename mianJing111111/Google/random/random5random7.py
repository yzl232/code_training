# encoding=utf-8
'''

Generate integer from 1 to 7 with equal probability

Given a function rand5() that returns integers from 1 to 5 with equal probability, write a function that returns integers from 1 to 7 with equal probability using rand5() only. Minimize the number of calls to rand5() method. Also, use of any other library function is not allowed and no floating point arithmetic allowed.



Solution:
We know rand5() returns integers from 1 to 5. How we can ensure that integers from 1 to 7 occur with equal probability?
If we somehow generate integers from 1 to a-multiple-of-7 (like 7, 14, 21, …) with equal probability, we can use modulo division by 7 followed by adding 1 to get the numbers from 1 to 7 with equal probability.

We can generate from 1 to 21 with equal probability using the following expression.

 5*rand5() + rand5() -5

 Let us see how above expression can be used.
1. For each value of first foo(), there can be 5 possible combinations for values of second foo(). So, there are total 25 combinations possible.
2. The range of values returned by the above equation is 1 to 25, each integer occurring exactly once.
3. If the value of the equation comes out to be less than 22, return modulo division by 7 followed by adding 1. Else, again call the method recursively. The probability of returning each integer thus becomes 1/7.


The below program shows that the expression returns each integer from 1 to 25


关键在于均匀分布。
'''
class Solution:
    def rand5(self):
        pass

    def rand7(self):      #和之前二进制的90%类似。  5进制模拟。    self.rand5() + 5* self.rand5()~~~6~30
        i = self.rand5() + 5* self.rand5() - 5   #这里-5是无所谓。  可以减去任何数。 只要模拟了5进制。25个值
        if i<=21:
            return i%7+1
        return self.rand7()
#注意。这里5*rand5是有理由的。要均匀分开。 均匀分在5个区间。每个区间
#为什么选21. 其实选7， 或者14，也是均匀的。 但是选21，概率要大些，不然可能要运行好久
class Solution2:
    def rand3(self):
        pass

    def rand5(self):
        i = self.rand3() + 3*self.rand3()  -3    # 4~12
        if i<=5: return i%5+1
        return self.rand5()