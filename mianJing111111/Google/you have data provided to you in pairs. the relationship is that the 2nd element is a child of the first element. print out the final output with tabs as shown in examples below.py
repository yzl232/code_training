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