# encoding=utf-8
#社交网络中，如何实现好友推荐。抽象成图，然后找出共同好友最多的那个人。


#社交网络中，如何实现好友推荐。抽象成图，然后找出共同好友最多的那个人。
class Node(object):   #2 nd hop.
    def __init__(self, val):
        self.val = val   #bfs两轮后，比较出现次数。 次数最多的就是了。
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
