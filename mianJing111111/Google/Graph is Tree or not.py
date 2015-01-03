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