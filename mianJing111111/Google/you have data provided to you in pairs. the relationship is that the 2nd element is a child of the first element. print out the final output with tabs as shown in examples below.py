# encoding=utf-8
'''
you have data provided to you in pairs. the relationship is that the 2nd element is a child of the first element.
print out the final output with tabs as shown in examples below

input: <a,b>
output: a
b

input: <a,b> <b,c> <d,c>
output: a
b
d
c

input: <a,b> <c,d>
output: a
c
b
d
'''

#因为不是graph。实际上有更简单的办法。  就是以下。  用BFS
#直接就说我有2种办法。  一种topoligical sort, 一种找root， 再BFS


#也有更简单的方法。 先找root
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



#
class Solution56:  #可以用hashmap  build 简单的node: children属性。
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
        if not root: return 0
        for x in root.children:   root.val +=self.dfs(x)
        return root.val