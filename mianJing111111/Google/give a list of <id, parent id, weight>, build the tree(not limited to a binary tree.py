# encoding=utf-8
'''
give a list of <id, parent id, weight>, build the tree(not limited to a
binary tree), then update each node’s sum value(sum is the sum of all its
descendents’ weights)
'''



class Relation:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child

class Solution:  #可以用hashmap  build 简单的node: children属性。
    def buildTree(self, relations):
        d = {};  notRoot = set()
        for rs in relations:
            if d[rs[0]] not in d:  d[rs[0]] = []
            d[rs[0]].append(rs[1])
            notRoot.add(rs[1])
        roots=[]    #找root
        for k in d.keys():
            if k not in notRoot:  roots.append(k)
        root = roots[0]

# 第二部分。 更新为sum of decendents
    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        self.dfs(root.right)
        if root.left: root.val+=root.left.val
        if root.right: root.val +=root.right.val