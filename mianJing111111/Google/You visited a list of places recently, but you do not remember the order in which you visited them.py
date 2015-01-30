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

# tickets 就是 edges。  根据ticktes建立图：  from的hashmap

class Solution:
    def topological(self, graph):   # 按题目输入，应当建一个hashmap.:    fromD = {}
        self.graph = graph
        self.ret,  self.visited = [], {}  # visited最开始为空。
        for k in graph:  self.dfs(k)
        return self.ret
    def dfs(self, x):
        if x in self.visited:   #已经visit过了
            if self.visited[x]==False: raise ValueError("cycle")  #发现了一个back edge。
            return
        self.visited[x] = False  #这就是与普通dfs的唯一不同。 用False标记
        for y in self.graph[x]:  self.dfs(y)
        self.ret.append(x)
        self.visited[x] = True


