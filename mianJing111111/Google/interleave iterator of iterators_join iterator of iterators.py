# encoding=utf-8
#超高频的一道题目了
'''
问的是和java里的iterator有关的问题：
假设有n （下面的例子n=3）个lists：
l1: a1 a2 a3 a4 a5 ...
l2: b1 b2 b3 b4...
l3: c1 c2 ....

要求交替输出：a1 b1 c1 a2 b2 c2....
给的输入是Iterator<Iterator<T>>,要实现一个
class InterleavingIterator<T>

刚开始脑子一团浆糊，太紧张了，过了有好几分钟才想清楚怎么写，（想的过程中漂亮的面试官还问我哪里卡住了，超级nice的），然后就写完了，然后面试官 说你要怎样测试你的code哇？ 然后我就给了几个test case，然后看test case的过程中发现代码有bug，没有处理输入为空的情况，改好了之后，又问了hasNext()和next()的时间复杂度，然后又聊了一下我的 work和她的work，然后就到时间了。






最有一轮总算是比较轻松了……第一题是写个iterator of a list of iterators，注意处理list为空和某个iterator为空的情况。代码没啥问题后，就进入了下一题。






6.加试电面, 写jump iterator类, 构造函数传入一个普通的iterator, 然后实现next(), hasNext(). next()返回传入iterator的next().next(), 就是每次跳过一个元素输出.
然后再实现一个rotateIterator(), 构造函数传入List<Iterator<T>>, 实现next(), hasNext(). 例如:
传入的三个iterator里面的值分别是[[1,2,3],[4,5,6], [7,8]], 那rotateIterator的next()应该输出[1,4,7,2,5,8,3,6]. 就是竖着遍历每个iterator输出, 如果当前的iterator没有了, 就跳到下一个.





2,面试官问我既然我在上一题用到了iterator，那接下来就编写一个变形的iterator吧：
给定两个iterator，让两个iterator进行交互输出。: [% m% V; x1 ~# ^
例子：
A:1234
B:abcd
则我编写的iterator输出为：1a2b3c4d，如果一个读完了那就读没读完那个直到两个都读完为止。


'''

#其实比较像用minHeap 那道题目
#用queue来做。 很巧妙

#http://stackoverflow.com/questions/9200080/join-multiple-iterators-in-java

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
        t = self.q.popleft()
        val = t.next()
        if t.hasNext(): self.q.append(t)
        return val