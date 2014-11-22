# encoding=utf-8
'''
Given a polygon with N vertexes and N edges. There is an int number(could be negative) on every vertex and an operation in set(*,+) on every edge. Every time, we remove an edge E from the polygon, merge the two vertexes linked by the edge(V1,V2) to a new vertex with value: V1 op(E) V2. The last case would be two vertexes with two edges, the result is the bigger one.
Return the max result value can be gotten from a given polygon.

'''