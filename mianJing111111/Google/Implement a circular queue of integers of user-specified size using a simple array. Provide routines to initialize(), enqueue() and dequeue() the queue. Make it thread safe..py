# encoding=utf-8
'''Implement a circular queue of integers of user-specified size using a simple array. Provide routines to initialize(), enqueue() and dequeue() the queue. Make it thread safe.
'''
#基本上就是+1  %， mod。  然后head==tail就是满了

import  threading

class circArray:
    def __init__(self, n):
        self.size = n
        self.head = 0
        self.tail = 0
        self.q = []
        self.myLock = threading.RLock()

    def enqueue(self, v):
        tmp = (self.tail+1) % self.size
        if tmp==self.head:   return False
        self.myLock.acquire()   #只要对class variable  变量操作之前加上lock就好
        self.q[self.tail] = v
        self.tail = tmp
        self.myLock.release()
        return True

    def dequeue(self):
        if self.head == self.tail: raise OverflowError('queue underflow')
        t = self.q[self.head]
        self.myLock.acquire()
        self.head = (self.head+1) % self.size
        self.myLock.release()
        return t