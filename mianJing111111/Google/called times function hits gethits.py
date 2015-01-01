# encoding=utf-8
import time
import random
from collections import  deque
import threading

#做法的话， 基本上都就是class的全局变量而已


#变化很多 。 各有不同



'''
统计函数调用次数
'''
class Solution:
    def __init__(self):
        self.count = 0
    def f(self):
        self.count+=1
s = Solution()
s.f()
s.f()
print s.count




'''
一分钟只能调用一次
'''
#做法。 lasttime.  大于60才更新
#一次比较特别。 只要比较上一次就好。  下面这个是N次。 除了比较lasttime,还要cnt
class Solution2:
    def __init__(self):
        self.lastTime = -1

    def add_money(self):
        curr_time = int(time.time())
        if curr_time - self.lastTime > 60:  #这已经是最好的办法。
            self.lastTime = curr_time
            pass

#设计一个function: bool cancall(), 保证每秒钟内return true的数量小于 N,

#做法。starttime,  <1的时候只更新cnt， >1的时候重置cnt, startTIme
class Solution3:
    def __init__(self, N):
        self.startTime = -1
        self.count = 0
        self.N = N

    def add_money(self):
        curr_time = int(time.time())
        if curr_time - self.startTime < 1 and self.count<self.N:
            self.count+=1  #不更新startTime
            pass
        elif curr_time-self.startTime>=1:
            self.count=1
            self.startTime = curr_time    #到这里更新
        else:  #过多了。 啥也不做
            pass

'''

类似于circular buffer in C++


circular queue

Make a data structure which is supposed to log number of user requests per second. At any point of time your boss can ask you the number of hits for the last 60 seconds.

随时调用，知道最近一分钟多少次？


Design a web counter to give how many hits per second, per minute and per hour (i.e., what kind of data structure and algorithm would you use to do this?).


keep track of every second.  And insert them to the queue.
伪代码

q = queue(maxLen=60)
Whenever a second is over:
    q.append(counts)
    counts = 0

foo():
    counts+=1

'''
#随时调用，知道最近一分钟多少次？
#G家的题目.
#可以进一步优化， 见Implement a counter that returns the number of function calls in the past minute
class Solution():
    def __init__(self):
        self.q = deque(maxlen = 60)
        self.curCount = 0
    def foo(self):
        self.curCount+=1

    def addToqueue(self):
        self.q.append(self.curCount)
        self.curCount=0

#每秒钟把当前的count加进去。
# circular queue

s = Solution()
while True:
    time.sleep(1)
    i = random.randint(1, 10)
    print "last minutes count:" + str(sum(s.q))
    print s.q
    if i>4: s.foo()
    s.addToqueue()
'''



统计最近30分钟google的top 10 searched keywords -- getTop10InLast30mins(),需
要经常调用。

用一个HashMap 来记得current minute 的
Keywords 和它的出现次数。


用 一个Queue of
size of 30 （因为30 分钟，也可以是60分钟）
来记录 每一分钟的top 10 的10-tuple的hashmap （只保留top10的记录），构成 一个动态leaking buffle Queue，
这样就可以精确
算出last 30 minutes, 60 minutes,  24 hours

freq Top K keywords.

'''





'''

circullar queue


下面这道变种题目;

问个题目，函数foo() 返回1或者０。 如果6０s内被调用1０次以上 返回1，否则０
不考虑多线程 怎么写这个好？

保留十个调用时间循环数组。最后减去第一个看是不是大于60秒
也是用queue.每次调用，插入时间按
'''
#巧妙
class Solution5:
    def __init__(self):
        self.q = deque([], maxlen=10)

    def foo(self):
        curTime = time.time()
        self.q.append(curTime)
        if len(self.q)==10 and self.q[-1]-self.q[0]<=60:      return 1
        return 0