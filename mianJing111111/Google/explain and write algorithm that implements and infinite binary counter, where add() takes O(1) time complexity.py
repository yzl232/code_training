# encoding=utf-8
'''
explain and write algorithm that implements and infinite binary counter, where add() takes O(1) time complexity
'''

'''
we keep an aggregation on consecutive 1 or 0.

meaning 111000111 is <3,1> <3,0> <3,1>

1) if the first bulk is of 1's. it turns to bulk of 0`s and turn the very next 0 to 1.

we now check if we can aggregate bulks of 1's.

2) if the first bulk is of 0's, we make the first digit 1. and see if we can aggregate 1's.
'''

#  写起来比较麻烦     #比较像serialize
class BinaryCounter:   #用array比较好写。 可以随时更改
    def __init__(self):
        self.stack = [[0, 1]]  #x[0]: 0 or 1,  x[1]:  数目

    def add1(self):
        if self.stack[-1][0]==0:   self.zerosPlus1()
        else:
            cur = self.stack.pop()
            if not self.stack:     self.stack.append([1, 1])
            else:   self.zerosPlus1()
            self.stack.append([0, cur[1]  ])

    def zerosPlus1(self):
        self.stack[-1][1]-=1
        if self.stack[-1][1]==0:  #当只有一个0 的时候， pop出来要考虑merge的问题
            self.stack.pop()
            if self.stack:  #merge 1
                self.stack[-1][-1]+=1
                return
        self.stack.append([1, 1])

    def restore(self):
        return ''.join([str(x[0])*x[1] for x in self.stack])

s = BinaryCounter()
for i in range(100):
    s.add1()
    print s.stack