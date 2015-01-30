# encoding=utf-8
#写一个filteredIterator， 给了你accept函数。
'''
发面经攒人品，求onsite啊。
写一个filteredIterator， 给了你accept函数。
interface Filter<T> {
boolean accepts(T t);
}

例子：
-1，-3，5，-5，-6
如果accept只接受正数的话
第一次call next()返回5，第二次的时候hasNext()就返回false了。各种edge case结果写到最后还是有bug
test case，大家写出来自己run，全空，全正，全负，正负夹杂正结尾，正负夹杂负结尾。我掉了正结尾的情况，结果就有个bug，面试官指出了才发现，感觉是不是要挂了……
而且由于没有看清楚函数的要求代码写的一点也不规范……，无语了啊。还是太紧张，真是……碰上G家就短路。希望面试官不要跟我一般见识给个过吧
'''

class Solution:
    def __init__(self, arr):
        self.i = 0  #和peek类似。  i取了类似top的作用。
        self.arr = arr
        self.findAccept()

    def hasNext(self):
        return self.i<len(self.arr)

    def next(self):
        t = self.arr[self.i]
        self.findAccept()
        return t

    def findAccept(self):
        while self.i<len(self.arr) and not self.accept(self.arr[self.i]):  self.i+=1

    def accept(self, x):
        pass