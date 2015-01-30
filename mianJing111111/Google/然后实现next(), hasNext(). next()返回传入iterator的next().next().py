# encoding=utf-8
'''
写jump iterator类, 构造函数传入一个普通的iterator, 然后实现next(), hasNext(). next()返回传入iterator的next().next(), 就是每次跳过一个元素输出.
'''
class IteratorPeek: #代码不长。可以背下
    def __init__(self, iterator):
        self.iterator = iterator  #因为隔2隔无法直接判断。所以用了一个nextO的变量. 提前了一格
        self.nextO = None
        self.advance()     #初始。 nextO

    def hasNext(self):
        return self.nextO!=None and self.iterator.hasNext()    #用！=None比较合适。  不然空字符，0， 之类。

    def next(self):
        assert  self.hasNext()
        t = self.iterator.next()  #2次
        self.advance()  #next O 更新
        return t

    def advance(self):
        if self.iterator.hasNext(): self.nextO = self.iterator.next()

#  1, 2, 3, 4, 5