# encoding=utf-8
#Implement Iterator class with peek() functionality in Java.
#出现好几次
'''
那题在板上说过，一个iterator，有next和hasNext，现在要你加个wrapper，使得
支持peek操作
'''
#非常高频的一道题目

# 提前一步
class IteratorPeek: #代码不长。可以背下
    def __init__(self, iterator):
        self.iter = iterator
        self.top = self.getTop()

    def hasNext(self):
        return self.top!=None

    def next(self):
        ret = self.top   # self. 设置空很关键.
        self.top = self.getTop()    #提前一步。 注意是自己的iter   #更新一个新的top
        return ret

    def getTop(self):
        return None if not self.iter.hasNext else self.iter.next()

    def peek(self):
        return self.top


'''
1.写一个Stream的interface, 就是有generic, 有peek(), next(), hasNext(), append()方法. 然后写一个merge List of sorted stream, 就是的k-way merge. 然后因为是generic, 传入参数要包括一个comparator.

'''
import heapq
class IteratorMerge: #代码不长。可以背下
    def __init__(self, arrs):
        self.arrs = arrs
        self.h =[(arrs[i][0], i, 0) for i in range(len(arrs)) if arrs[i]]
        heapq.heapify(self.h)

    def hasNext(self):
        return self.h!=None

    def next(self):
        if not self.hasNext():   raise ValueError("End of iterator")
        val, i, j = heapq.heappop(self.h)
        if j+1<len(self.arrs[i]):  heapq.heappush(self.h, (self.arrs[i][j+1], i, j+1))
        return val

# 像这种iterator都是那种把while 循环 分拆成一步一步的。  只要把while循环的几句抄到Next即可。
# while的条件就是 has Next

#和下面的k way merge一模一样。。。


'''
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, arrs):
        h =[(arrs[i][0], i, 0) for i in range(len(arrs)) if arrs[i]]
        heapq.heapify(h);  ret = []
        while h:
            val, i, j = heapq.heappop(h)
            ret.append(val)
            if j+1<len(arrs[i]):  heapq.heappush(h, (arrs[i][j+1], i, j+1))
        return ret   #复杂度 O(nkLogk) 是最优解
'''