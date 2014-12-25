# encoding=utf-8
'''
You visited a list of places recently, but you do not remember the
order in which you visited them. You have with you the airplane
tickets that you used for travelling. Each ticket contains just the
start location and the end location. Can you reconstruct your journey?
'''

# 二元输入。 找链接。。
#想了想，确实是topological sort. 只不过没有
'''
If there is loop, more than one solution.
We should first start with no loop situation.
'''

class Solution:
    def topological(self, graph):
        self.graph = graph
        self.ret,  self.visited = [], {}
        for k in graph.keys():  self.dfs(k)
        return self.ret
    def dfs(self, node):
        if node in self.visited:   #已经visit过了
            if self.visited[node]==False: raise ValueError("cycle")  #发现了一个back edge。
            return
        self.visited[node] = False  #这就是与普通dfs的唯一不同。 用False标记
        for k in self.graph[node]:  self.dfs(k)
        self.ret.append(node)
        self.visited[node] = True


