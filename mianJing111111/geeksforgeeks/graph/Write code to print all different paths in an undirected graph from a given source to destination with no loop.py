# encoding=utf-8
'''
Given a undirected graph, source and destination, write the code to find the total number of distinct nodes visited, considering all possible paths.

普通的DFS题目。

假如题目给的时   node,  neighbours. 只要我手动把它们转换成二元组就好。



Write code to print all different paths in an undirected graph from a given source to destination with no loop(any node can be at most once in a path ).

'''
# F家题目





#复制了有向图， 稍微修改
class Solution3:
    def paths(self, root):
        self.rets = []
        self.dfs(root, set([root]), [root])
        return self.rets

    def dfs(self, node, visited, cur):  #visited传进去。 这是一个特别的地方。
        if node.neighbors:   #空， 或者visited过了
            self.rets.append(cur)
            return
        for n in node.neighbors:
            if n in visited: continue
            t= visited.copy(); t.add(n)
            self.dfs(n, t, cur+[n])



'''
class Solution3:
    def paths(self, start, end):
        self.paths = []; self.end = end
        self.dfs([], start, {})
        return len(set(tuple(self.paths)))

#[1, 2],  [2, 8],  [1,  8]
    def dfs(self, cur, node, visited):  #visited传进去。 这是一个特别的地方。
        if cur[-1] ==self.end:
            self.paths.append(cur)
            return
        for x in node.neighbors:
                if x in visited: continue   #不能再这里操作。 因为每个循环for。 visited是相互独立的。
                t = visited.copy(); t[node]=1
                self.dfs(cur+[node], x, t)
#比环还要容易很多。比较单纯


例子  1--2---3
        1---2----9----3  都是合法的。 如果是self.visited， 就不合适。

'''