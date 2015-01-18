# encoding=utf-8
'''
Given a set of busy time intervals of two people as in a calendar, find the free time intervals of both the people so as to arrange a new meeting
input: increasing sequence of pair of numbers
per1: (1,5) (10, 14) (19,20) (21,24) (27,30)
per2: (3,5) (12,15) (18, 21) (23, 24)
ouput: (6,9) (16,17)  (25,26)
'''
#一个简单做法。  calendar总共才30。  用2个hashtable存就好。
class Solution:
    def find(self, arr1, arr2):
        d1, d2, free= self.getSet(arr1), self.getSet(arr2), []
        for x in range(1, 31):
            if x not in d1 and x not in d2:
                free.append(x)
        i=0; ret=[]
        while i<len(free):
            start=free[i]
            while i+1<len(free) and free[i]==free[i+1]-1:     i+=1
            end=free[i]
            i+=1
            ret.append((start,end))
        return ret

    def getSet(self, arr):
        d=set([])
        for i, j in arr:
            for x in range(i, j+1):
                d.add(x)
        return d
s = Solution()
print s.find([(1,5) ,(10, 14), (19,20), (21,24), (27,30)],  [(3,5), (12,15), (18, 21), (23, 24)])


#通用法。 先找到free Intervals for both。 然后找intersect

def intersect(arr1, arr2):  # intersection of 2 sorted array变体
    i=j=0; ret = []
    while i<len(arr1) and j<len(arr2):
        s1, e1=arr1[i];  s2, e2=arr2[j]
        if s2>e1: i+=1
        elif s1>e2: j+=1
        else:
            i+=1; j+=1
            ret.append((max(s1, s2), min(e1, e2)))
    return ret+arr1[i:]+arr2[j:]
print intersect([(1,5) ,(10, 14), (19,20), (21,24), (27,30)],  [(3,5), (12,15), (18, 21), (23, 24)])