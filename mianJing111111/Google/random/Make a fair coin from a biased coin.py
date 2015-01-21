# encoding=utf-8
'''
You are given a function foo() that represents a biased coin. When foo() is called, it returns 0 with 60% probability, and 1 with 40% probability. Write a new function that returns 0 and 1 with 50% probability each. Your function should use only foo(), no other library method.

调用情况， 00,11,01,,10概率 0.36, 0.16, 0.24, 0.24
'''
class Solution:
    def foo(self):
        pass

    def myFoo(self):
        val1 = self.foo()
        val2 = self.foo()
        if val1==0 and val2==1: return 0
        if val1==1 and val2==0: return 1
        return self.myFoo()