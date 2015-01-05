# encoding=utf-8
'''
有向图
Graph is Tree or not
We know that every Tree is a graph but reverse is not always true. In this problem, we are given a graph and we have to find out that whether it is a tree topology or not?
There can be many approaches to solve this problem, out of which we are proposing one here.

    If number of vertices is n and number of edges is not n-1, it can not be a tree.
    If it has n-1 edges also, then check for connected components.
        If there are more than one components, there must be some cycle(s) in some of the components. Hence it is not a tree.

For connected components, here we are using FIND-UNION technique.
In this method there is a parent array for each vertex, initialized to -1.
For each edge, we find the parent of both vertices.

    If both have same parent, then it means they belong to the same component and hence there is a cycle.
    Otherwise, join these two components by changing the parent of one of the vertex, of edge, to the parent of other vertex.

'''
#每次都找root(没有ingoing edge 的node)。 多于一个node。不是.    然后BFS。 如果已经出现过了。 不是tree
#If number of vertices is n and number of edges is not n-1, it can not be a tree.

#和这道题目像。build_tree_from_array
class Relation:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child

class Solution:  #可以用hashmap  build 简单的node: children属性。
    def buildTree(self, relations):
        d = {};  notRoot = set()
        for rs in relations:
            if d[rs[0]] not in d:  d[rs[0]] = []
            d[rs[0]].append(rs[1])
            notRoot.add(rs[1])
        roots=[]    #找root
        for k in d.keys():
            if k not in notRoot:  roots.append(k)
        if len(roots)!=1: return False
        root = roots[0]
        self.d = d
        self.bfs(root)

    def bfs(self, root):
        pre, found = [root], set([root])   # 除了pre, cur之外，还用了第三个vals
        while pre:
            cur, vals = [], []     #必须用array。 因为是有序的。 并且不会有重复
            for node in pre:
                if node not in self.d: continue
                for x in self.d[node]:
                    if x in found: return False
                    found.add(x);  cur.append(x)
            pre = cur
        return True