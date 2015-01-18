# encoding=utf-8
'''
Given a family tree for a few generations for the entire population and two people write a routine that will find out if they are blood related. Siblings are blood related since they have the same parents. Cousins are blood related since one of their parents have the same parents etc. Design the data structure first and then write the routine.
'''
class Person:
    def __init__(self, p1, p2):
        self.p1=p1
        self.p2 = p2

# find lca.
#有2个parent节点的lca。
#同时BFS.  放hashtable。
#就是有parent节点的做法

class Solution:
    def find_Ancestor(self, p, q):
        anc1 = set();  anc2=set()
        pre1 = []; pre2=[]
        while pre1 or pre2:
            if pre1:
                cur1 = []
                for x in pre1:
                    if x.p1 in anc2 or x.p2 in anc2: return True
                    cur1.append(x.p1); cur1.append(x.p2)
                    anc1.add(x.p1); anc1.add(x.p2);
                pre1 = cur1
            if pre2:
                cur2 = []
                for x in pre2:
                    if x.p1 in anc1 or x.p2 in anc1: return True
                    cur2.append(x.p1); cur2.append(x.p2)
                    anc2.add(x.p1); anc2.add(x.p2)
                pre2 = cur2
        return False




#同时BFS. 可以对比一下lca。很类似。

class Solution3:
    def find_Ancestor(self, p, q):
        d = {}
        while p or q:
            if p:
                if p in d: return p
                d[p] = 1
                p = p.parent
            if q:
                if q in d: return q
                d[q] = 1
                q = q.parent
        return