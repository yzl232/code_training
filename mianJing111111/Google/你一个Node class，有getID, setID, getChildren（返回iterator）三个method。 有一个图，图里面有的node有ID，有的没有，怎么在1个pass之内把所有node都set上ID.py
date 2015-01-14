# encoding=utf-8
'''
你一个Node class，有getID, setID, getChildren（返回iterator）三个method。 有一个图，图里面有的node有ID，有的没有，怎么在1个pass之内把所有node都set上ID
'''



'''
 我的做法是用一个hashmap<Integer, Node>，

  每遇到一个没有ID的Node，分配给他一个ID，把node保存下来，没遇到一个有ID的node，查一下ID是不是已经在hashmap里了，

  如果已存在，就把hashmap里的那个node的id改一下
'''
class Solution:
    N=1
    def solve(self, graph):
        self.d=d={}
        for x in graph:
            id = x.getID
            if id:
                if id in d:
                    y = d[id]
                    newID=self.idGenerater()  #冲突了。 重新设置
                    y.setID(newID)
                    d[newID]=y
                d[id]=x
            else:
                newID = self.idGenerater()
                x.setID(newID)
                d[newID]=y

    def idGenerater(self):
        while self.N in self.d:   self.N+=1
        return self.N