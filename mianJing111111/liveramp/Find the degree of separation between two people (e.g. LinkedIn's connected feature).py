# encoding=utf-8
'''
Find the degree of separation between two people (e.g. LinkedIn's connected feature)

n
d

'''
class People:
    def __init__(self, id, friends):
        self.id = id
        self.friends = []

class Solution:
    def findDegree(self, x, y):
        visited1 = {x:0}; visited2 = {y:0}
        candidates1 = set([x])
        candidates2 = set([y])
        step = 1
        while len(candidates1)>0 and len(candidates2)>0:
            current1 = set([])
            current2 = set([])
            for i in candidates1:
                for p in i:
                    if p not in visited1:
                        if p in visited2:
                            return step+visited2[p]
                        else:
                            visited1[p] = step
                            current1.add(p)
            for i in candidates2:
                for p in i:
                    if p not in visited2:
                        if p in visited1:
                            return step+visited1[p]
                        else:
                            visited2[p] = step
                            current2.add(p)
            candidates1 = current1
            candidates2 = current2