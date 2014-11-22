#DFS is more common. BFS can find the shortest path
#BFS uses while loop. DFS uses recursion

__author__ = 'zhenglinyu'
def BFS(s, adj):
    level = {}
    level[s] = 0
    parent = {}
    parent[s] = None
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i+=1



parents = {}
def DFS(V, adj):
    parents = {}
    for s in V:
        if s not in parents:
            parents[s] = None
            DFS_visit(adj, s)

def DFS_visit( adj, s):
    for i in adj[s]:
        if i not in parents:
            parents[i] = s
            DFS_visit( adj, i)
