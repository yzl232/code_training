# encoding=utf-8
'''
Friend Suggestion，知道一个人在network里的Friends，求Friends的Friends里和这个人最多common friends的人
'''

# O(n2)
class Solution:
    def find(self, a):
        ret = (0, None)
        setA = set(a.friends)
        for x in a.friends:
            cnt = 0
            for y in x.friends:
                if y in setA:  cnt+=1
            if cnt>ret[0]: ret = (cnt, x)
        return x