# encoding=utf-8
#社交网络中，如何实现好友推荐。抽象成图，然后找出共同好友最多的那个人。
class Node(object):
    def __init__(self, val):
        self.val = val
        self.friends = []

def recommend(node):
    exclude = set(node.friends + [node])
    freq = {}
    for x in node.friends:
        for y in x.friends:
            if y not in exclude:
                freq[y] = freq.get(y, 0) + 1
    ret = (None, 0)
    for key, val in freq.items():
        if val>ret[1]: ret=(key, val)
    return ret[1]