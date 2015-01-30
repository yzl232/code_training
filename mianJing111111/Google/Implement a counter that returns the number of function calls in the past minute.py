# encoding=utf-8
'''
Implement a counter that returns the number of function calls in the past minute
'''
from collections import deque

class Solution():
    def __init__(self):
        self.q = deque(maxlen = 60)
        self.curCount = 0
        self.s = None

    def foo(self):
        self.curCount+=1

    def set(self):
        if len(self.q)==60:
            if not self.s: self.s = sum(self.q)
            self.s+=self.curCount-self.q[0]
        self.q.append(self.curCount)
        self.curCount=0

    def get(self):
        return self.s     #可以进一步优化60倍的。 略去。..