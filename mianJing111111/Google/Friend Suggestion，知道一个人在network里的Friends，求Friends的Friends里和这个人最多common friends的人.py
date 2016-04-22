# encoding=utf-8
'''
Friend Suggestion，知道一个人在network里的Friends，求Friends的Friends里和这个人最多common friends的人
'''
# 理清楚一下题意
# O(n2)
# friends suggestions超高频

# encoding=utf-8
#社交网络中，如何实现好友推荐。抽象成图，然后找出共同好友最多的那个人。
class Node(object):   #2 nd hop.
    def __init__(self, id):
        self.id = id   #bfs两轮后，比较出现次数。 次数最多的就是了。
        self.friends = []

def recommend(node):
    exclude = set(node.friends + [node]);  cnt = {}
    for x in node.friends:
        for y in x.friends:
            if y not in exclude:
                if y not in cnt: cnt[y]=0
                cnt[y] += 1
    return max((val, key) for key, val in cnt.items())

#只用了O(n2)的复杂度

'''
class Solution:
    def find(self, a):
        ret = (0, None)
        setA = set(a.friends);  fFriends=set()   #复杂度。 平均是O(n3). . 单第二层 FFriends就有n2个。
        for x in setA:    # 1-st hop
            for y in x.friends:  #  2-nd hop
                if y not in setA and y!=a: fFriends.add(y)# prune掉已经是朋友以及自己
        for x in fFriends:
            cnt=0
            for y in x.friends:
                if y in setA: cnt+=1
            ret = max(ret, (cnt, x))
        return ret
'''