# encoding=utf-8
'''


Count all possible walks(paths) from a source to a destination with exactly k edges

Given a directed graph and two vertices ‘u’ and ‘v’ in it, count all possible walks from ‘u’ to ‘v’ with exactly k edges on the walk.

The graph is given as adjacency matrix representation where value of graph[i][j] as 1 indicates that there is an edge from vertex i to vertex j and a value 0 indicates no edge from i to j.

For example consider the following graph. Let source ‘u’ be vertex 0, destination ‘v’ be 3 and k be 2. The output should be 2 as there are two walk from 0 to 3 with exactly 2 edges. The walks are {0, 2, 3} and {0, 1, 3}
O(n**k)

'''

# 用memoization 就好。

class Solution:
    def countWalks(self, graph, u, v, k):
        if k==0 and u==v: return 1  #
        if k==1 and graph[u][v]: return 1
        if k<=0: return 0  #注意确实要放在这里比较好
        cnt = 0
        for i in range(len(graph)):
            if i==u or i==v: continue
            if graph[u][i]: cnt+=self.countWalks(graph, i, v, k-1) #u=>i=>v         1+ k-1 steps
        return cnt


'''
dp

O(n3*k)
'''
class Solution2:
    def countWalks(self, graph, u, v, k):
        n = len(graph)
        dp = [[[0 for i in range(n)]for j in range(n)]for p in range(k+1)]
        for e in range(k+1):
            for i in range(n):
                for j in range(n):
                    if e==0 and i==j: dp[e][i][j]=1
                    elif e==1 and graph[i][j] : dp[e][i][j] = 1
                    elif e>1:
                        for a in range(n):
                            if a==j or a==i: continue
                            if graph[i][a]:  dp[e][i][j] += dp[e-1][a][j]  #1+ k-1 steps   i=>a=>j
        return dp[-1][u][v]
