# encoding=utf-8
#Implement Iterator class with peek() functionality in Java.
#出现好几次
'''
那题在板上说过，一个iterator，有next和hasNext，现在要你加个wrapper，使得
支持peek操作
'''

class IteratorPeek: #代码不长。可以背下
    def __init__(self, iterator):
        self.iterator = iterator
        self.top = None
        self.getTop()

    def hasNext(self):
        return self.top!=None

    def next(self):
        if not self.hasNext(): return
        if not self.top: raise EOFError("End of iterator")
        ret = self.top
        self.getTop()
        return ret

    def getTop(self):
        if not self.top: self.top = self.iterator.next()