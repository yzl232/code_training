# encoding=utf-8
'''
有N个node,每个都不停的向外发送timestamps,具体发送哪些timestamp是每个node决定的,从其他node来说是随机的.现在要 收集这些node发送的所有timestamp.如果某个timestamp被发现从超过99%的node上发送出来,记录下来.需要怎么做?这些 timestamp很多,是不能完全放进去内存里面的.如果node非常多,怎么scale?
我给的方案是用HashMap<Timestamp, count>,分布存到多台机器上面。阿三表示数据很多，每台机器的内存都存不下，让我优化。我的进一步方案是再设定一个时限T，过期的数据可以丢 掉。阿三要求进一步优化。我的再进一步方案是对于这个时限T再分割成n个小格。这个n需要通过实验根据具体实际情况来确定。如果在T／n时间里面，某些 Timestamp的count小于某个设定值，比如0.01N，认为这个timestamp被收集到0.99N的可能性已经趋近于0，可以忽略了，从 HashMap里面删除。最后阿三还是表示不满意，不能完全理解我的方案。
'''



'''
设计题是TSD，常用于monitoring/alarming系统 不需要hash某个timestamp，弄些
bucket，每分钟，每5分钟之类的，循环数组过期persist就行，redis可以
'''
# 一个办法就是hash后， %1000 到多个机器。但是面试官说不好。
#那么用circular buffer
# 关键2点。 1 肯定要用hashtable记录node， value是【nodes...】的。  2 要circular queue.每分钟
from collections import  deque
NodeN=1000
class Solution():
    def __init__(self):
        self.q = deque(maxlen = 60)
        self.curCount = {}

    def foo(self, timeStamp, nodeID):
        self.curCount.add(timeStamp, nodeID)

    def addToqueue(self):
        self.q.append(self.curCount)
        self.curCount=set([])

    def check(self):  #每分钟调用一次check函数，。 merge这一分钟的hashtable。 check出不符合的。
        d = {}
        for x in self.q:
            for key in x:
                if key not in d: d[key] = set([])
                d[key].update(x[key])
        for key in d:
            if len(d[key])>=0.99*NodeN:  print key
#circular buffer每个存set。 存1分钟的。 然后每分钟check这一分钟的。

