# encoding=utf-8
'''
What is the maximum number of edges you could add to n vertexes to make a acyclic undirected graph?

Follow up:
What is the maximum number of edges you could add to n vertexes to make a acyclic directed graph?
'''




'''
Acyclic undirected graph:

V-1 edges. Spanning tree of the graph.


Acyclic directed graph:

Imagine the graph topologically sorted. It can only have edges going down (from top to bottom), otherwise it would have cycles.

The way to maximize the number of edges without creating cycles is to connect a given vertex to all other vertices that are below it (again, imagining the graph in a topological order). For instance, the vertex 0 is connected to 1, 2, 3, ..., V-1; vertex 1 to 2, 3, ..., V-1. So on and so forth.

Therefore, the total number of edges is: Sum (i=0 to V-1) i, which is equal to (V^2-V)/2.
'''

# sum( 0.....V-1. ) -  number of edges already