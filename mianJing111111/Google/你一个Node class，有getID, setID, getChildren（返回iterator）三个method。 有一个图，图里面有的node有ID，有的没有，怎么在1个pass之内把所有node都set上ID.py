# encoding=utf-8
'''
你一个Node class，有getID, setID, getChildren（返回iterator）三个method。 有一个图，图里面有的node有ID，有的没有，怎么在1个pass之内把所有node都set上ID
'''



'''
 我的做法是用一个hashmap<Integer, Node>，

  每遇到一个没有ID的Node，分配给他一个ID，把node保存下来，没遇到一个有ID的node，查一下ID是不是已经在hashmap里了，

  如果已存在，就把hashmap里的那个node的id改一下
'''


#怎样做到一个pass给所有都标上unique的ID。  先标上一个没出现的。  如果后来发现出现了。。于是hashmap找到它。重新标。
class Solution:
    N=1
    def solve(self, graph):
        self.d=d={}
        for x in graph:
            id = x.getID()
            if id:
                if id in d:  self.idGenSet(d[id])  #冲突了。 重新设置
                d[id]=x
            else:  self.idGenSet(x)

    def idGenSet(self, x):
        while self.N in self.d:   self.N+=1
        self.d[self.N]=x