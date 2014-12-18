# encoding=utf-8
'''
Following is a simple algorithm to find out whether a given graph is Birpartite or not using Breadth First Search (BFS).
1. Assign RED color to the source vertex (putting into set U).
2. Color all the neighbors with BLUE color (putting into set V).
3. Color all neighbor’s neighbor with RED color (putting into set U).
4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2.
5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot be colored with 2 vertices (or graph is not Bipartite)
'''
#思想就是所有node和它的邻居颜色必须不同
class Solution:
    def isBiparty(self, graph, src):
        colors = {src: 0}
        pre = set([src])
        while pre:
            cur = set([])
            for n in pre:
                for x in n.neighbors:
                    if x not in colors:
                        cur.add(x)
                        colors[x]=1-colors[n]
                    else:
                        if colors[x]==colors[n]: return False
            pre = cur
        return True

'''
#graph。 BFS都是用一个hashmap代替visited。   然后
for n in pre:
for n in x.neigbors.
 if not in map
'''