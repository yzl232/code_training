# encoding=utf-8
#Implement Iterator class with peek() functionality in Java.
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