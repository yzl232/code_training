# encoding=utf-8
'''
give a list of <id, parent id, weight>, build the tree(not limited to a
binary tree), then update each node’s sum value(sum is the sum of all its
descendents’ weights)
'''

#出现过好多次。  用简单的找root的方法就好。
class Solution:
    def topological(self, arr):  #基本一样。 就是花几行build一下graph
        graph = {}
        for x in arr:
            if x[1] not in graph: graph[x[1]] = []
            graph[x[1]].append(x[0])
        self.ret,  self.visited = [], {};  self.graph = graph
        for k in graph.keys():  self.dfs(k)
        return self.ret

    def dfs(self, x):
        if x in self.visited:   #已经visit过了
            if self.visited[x]==False: raise ValueError("cycle")  #发现了一个back edge。
            return
        self.visited[x] = False  #这就是与普通dfs的唯一不同。 用False标记
        for k in self.graph[x]:  self.dfs(k)
        self.ret.append(x)
        self.visited[x] = True


#因为不是graph。实际上有更简单的办法。  就是以下。  用BFS
#直接就说我有2种办法。  一种topoligical sort, 一种找root

class TreeNode:
    def __init__(self, x, ):
        self.val = x
        self.children = []

class Relation:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child

class Solution:  #可以用hashmap  build 简单的node: children属性。   #也就是hashtable based..    tree
    def buildTree(self, relations):
        d = {};  notRoot = set()
        for rs in relations:
            if d[rs[0]] not in d:  d[rs[0]] = []
            d[rs[0]].append(rs[1])
            notRoot.add(rs[1])
        roots=[]    #找root
        for k in d.keys():
            if k not in notRoot:  roots.append(k)



# 第二部分。 更新为sum of decendents
    def dfs(self, root):
        for x in root.children:   root.val +=self.dfs(x)
        return root.val

'''
    def dfs(self, root):
        if not root: return 0
        root.val+=self.dfs(root.left)+self.dfs(root.right)
        return root.val
'''