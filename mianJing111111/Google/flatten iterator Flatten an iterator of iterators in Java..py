# encoding=utf-8

#implement hasNext and next for a list of lists

#G家高频
'''
实现一个FlattenIterator，构造函数的传入参数是Iterator<Iterator<T>>.

class FlatternIterator<T>{
     public FlatternIterator(Iterator<Iterator<T>> iterators){

     }
    public boolean hasNext(){

    }
    public T next(){

   }
}

例如传入的是
{
    {1,2,3}
    {4,5}
    {6,7}
}
则如果一直next输出，则输出 1,2,3,4,5,6,7
'''
from collections import  deque
class FlatIterator:
    def __init__(self, iters):
        self.q= deque(iters)

    def hasNext(self):
        while self.q:
            if self.q[0].hasNext(): return True
            self.q.popleft()
        return False

    def next(self):
        return self.q[0].next()


#用queue也可以做。




class FlatIterator:
    def __init__(self, iters):
        self.i = 0
        self.iters = iters

    def hasNext(self):
        if self.i>=len(self.iters): return False
        if self.iters[self.i].hasNext(): return True
        self.i+=1
        return self.hasNext()  #递归

    def next(self):
        return self.iters[self.i].next()




'''
给出一个二维vector，实现 flatten类
class flatten implements iterator{
  public flatten(vector<vector<int>> a);
  boolean hasNext();
  iterator next();
'''

#Program an iterator for a List which may include nodes or List  i.e.  * {0,
# {1,2}, 3 ,{4,{5, 6}}} Iterator returns 0 - 1 - 2 - 3 - 4 - 5 - 6"
#Flatten an iterator of iterators in Java. If the input is [ [1,2], [3,[4,5]], 6], it should return [1,2,3,4,5,6]. Implement hasNext()
#
# I am not comfortable wring Java right now.  Do you mind me writing normal python code ?  I feel the idea is the similar.

#用stack肯定是面试官喜欢的做法。 这肯定是正确的。


#下面这个实际上是iterator of list or just nodes .  并不是an iterator of iterators。
#下面是linkedin的 deep     iterator
class DeepIterator: #代码不长。可以背下
    def __init__(self, l):
        self.stack = [l]
        self.advanceToNext()

    def hasNext(self):
        if not self.stack: return False
        return True

    def next(self):
        if not self.hasNext(): return
        result = self.stack.pop()
        self.advanceToNext()
        return result

    def advanceToNext(self):
        if self.stack and isinstance(self.stack[-1], list):  #加入第一个一直是iterator。就一直解开。
                cur = self.stack.pop()
                self.stack+=cur[::-1]
                self.advanceToNext()



d = DeepIterator( [ [1,2],[], [3,[4,5]], 6])
while d.hasNext():
    print d.next()




class Solution:
    def flatten(self, arr):
        result = []
        for i in arr:
            if isinstance(i, list):  result+=self.flatten(i)
            else:  result.append(i)
        return result
s = Solution()
print s.flatten( [ [1,2], [3,[4,5]], 6])
