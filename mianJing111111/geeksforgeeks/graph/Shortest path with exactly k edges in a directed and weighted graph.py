# encoding=utf-8
'''


Shortest path with exactly k edges in a directed and weighted graph

Given a directed and two vertices ‘u’ and ‘v’ in it, find shortest path from ‘u’ to ‘v’ with exactly k edges on the path.

The graph is given as adjacency matrix representation where value of graph[i][j] indicates the weight of an edge from vertex i to vertex j and a value INF(infinite) indicates no edge from i to j.

For example consider the following graph. Let source ‘u’ be vertex 0, destination ‘v’ be 3 and k be 2. There are two walks of length 2, the walks are {0, 2, 3} and {0, 1, 3}. The shortest among the two is {0, 2, 3} and weight of path is 3+6 = 9.

graph1

The idea is to browse through all paths of length k from u to v using the approach discussed in the previous post and return weight of the shortest path. A simple solution is to start from u, go to all adjacent vertices and recur for adjacent vertices with k as k-1, source as adjacent vertex and destination as v. Following is C++ implementation of this simple solution.

这里我假定没有graph[u][v]就是权值。  权值为空，则没有path
'''

class Solution:
    def countWalks(self, graph, u, v, k):
        self.result = 10**10
        self.dfs(graph, u, v, k, 0)
        return self.result

    def dfs(self, graph, u, v, k, tmpResult):
        if k==0 and u==v:
            self.result = min(self.result, tmpResult)
            return
        if k==1 and graph[u][v] != None:
            self.result = min(self.result, tmpResult+ graph[u][v])
            return
        if k<=0: return None  #注意确实要放在这里比较好
        for i in range(len(graph)):
            if graph[u][i] != None:
                if u!=i and v!=i:
                    self.dfs(graph, i, v, k-1, tmpResult+graph[u][i]) #u=>i=>v         1+ k-1 steps



'''
dp

O(n3k)
'''
class Solution2:
    def countWalks(self, graph, u, v, k):
        n = len(graph)
        dp = [[[None for i in range(n)]for j in range(n)]for p in range(k+1)]
        for e in range(k+1):
            for i in range(n):
                for j in range(n):
                    if e==0 and i==j: dp[e][i][j]=1
                    elif e==1 and graph[i][j] != None: dp[e][i][j] = 1
                    elif e>1:
                        for a in range(0, n):
                            if i==a or j==a: continue
                            if graph[i][a]:
                                dp[e][i][j]= min(dp[e-1][a][j]+graph[i][a],  dp[e][i][j]) #1+ k-1 steps   i=>a=>j
        return dp[-1][u][v]