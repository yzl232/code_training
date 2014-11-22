# encoding=utf-8
'''
Given a undirected graph, source and destination, write the code to find the total number of distinct nodes visited, considering all possible paths.

普通的DFS题目。

假如题目给的时   node,  neighbours. 只要我手动把它们转换成二元组就好。



Write code to print all different paths in an undirected graph from a given source to destination with no loop(any node can be at most once in a path ).

'''


class Solution3:
    def paths(self, start, end):
        self.paths = []; self.end = end
        self.dfs([start], start, {})
        a = set()
        for path in self.paths:
            for n in path:
                a.add(n)
        return len(a)

#[1, 2],  [2, 8],  [1,  8]
    def dfs(self, tmpPath, node, visited):  #visited传进去。 这是一个特别的地方。
        visited[node]=1
        if tmpPath[-1] ==self.end:
            self.paths.append(tmpPath)
            return
        for n in node.candidates:
                if n in visited: continue   #不能再这里操作。 因为每个循环for。 visited是相互独立的。
                self.dfs(tmpPath+[n], node, visited.copy())
'''

例子  1--2---3
        1---2----9----3  都是合法的。 如果是self.visited， 就不合适。

'''