# encoding=utf-8
'''Implement a circular queue of integers of user-specified size using a simple array. Provide routines to initialize(), enqueue() and dequeue() the queue. Make it thread safe.
'''
#基本上就是+1  %， mod。  然后head==tail就是满了

import  threading
myLock=threading.RLock()
class circArray:  #为了统一lock。 同时还singleton
    def __init__(self, n):
        self.n = n
        self.head = 0;  self.tail = 0
        self.q = [None]*n
        self.curSize=0  #用了这个。 容易了很多。
        global myLock

    def enqueue(self, v):
        myLock.acquire()  # 我觉得还是简单粗暴的放最前面。 #只要对class variable  变量操作之前加上lock就好
        if self.curSize==self.n:  raise ValueError("queue full")
        self.q[self.tail] = v
        self.tail = (self.tail+1) % (self.n+1)
        self.curSize+=1
        myLock.release()
        return True

    def dequeue(self):
        myLock.acquire()
        if self.curSize==0: raise ValueError('queue underflow')
        t = self.q[self.head]
        self.head = (self.head+1) % (self.n+1)
        self.curSize-=1
        myLock.release()
        return t