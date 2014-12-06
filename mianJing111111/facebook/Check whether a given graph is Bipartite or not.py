# encoding=utf-8
'''
Following is a simple algorithm to find out whether a given graph is Birpartite or not using Breadth First Search (BFS).
1. Assign RED color to the source vertex (putting into set U).
2. Color all the neighbors with BLUE color (putting into set V).
3. Color all neighbor’s neighbor with RED color (putting into set U).
4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2.
5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot be colored with 2 vertices (or graph is not Bipartite)
'''
class Solution:
    def isBiparty(self, graph, src):
        colors = {node:None for node in graph}
        colors[src] = 0
        candidates = set([])
        while candidates:
            current = set([])
            for n in candidates:
                for neighbor in n:
                    current.add(neighbor)
                    if not colors[neighbor]:   colors[neighbor]=1-colors[n]  #neighbor一定相反
                    elif colors[neighbor] == colors[n]: return False
            candidates = current