# encoding=utf-8
'''
写jump iterator类, 构造函数传入一个普通的iterator, 然后实现next(), hasNext(). next()返回传入iterator的next().next(), 就是每次跳过一个元素输出.
'''
class IteratorPeek: #代码不长。可以背下
    def __init__(self, iterator):
        self.iterator = iterator
        self.nextO = None
        if iterator.hasNext(): self.nextO = iterator.next()      #初始。 nextO

    def hasNext(self):
        if not self.nextO or not self.iterator.hasNext(): return False
        return True

    def next(self):
        t = self.iterator.next()
        if self.iterator.hasNext(): self.nextO = self.iterator.next()  #next O 更新
        return t