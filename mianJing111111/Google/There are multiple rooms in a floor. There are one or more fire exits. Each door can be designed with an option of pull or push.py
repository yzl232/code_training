# encoding=utf-8
'''
There are multiple rooms in a floor. There are one or more fire exits. Each door can be designed with an option of pull or push. For fire safety, a door should be designed so as to open (push) towards the fire exit.
Design a data structure to represent the floor and door design.  A person could start from any room and moves towards fire exit. Write an algorithm to check if all the doors are designed to be pushed towards fire exit.
'''



'''
I think a DAG will do it. Also, to check reverse all the edge-directions and do DFS/BFS from fire-exit. If you're able to reach all of the doors from fire-exit. Bingo!
'''




'''
Problem is not very clear. Still, I came up with a solution.

Construct a graph where the vertices are the rooms, corridors, and fire exits; and the edges are the doors. Naturally these edges are directed in the same way as the corresponding doors.

For the floor design to be valid, any vertex of fire exit should be reachable from every vertex of room.

Reachability in planar graphs (which is the case here) can be computed in O(VlogV) using Thorup's Algorithm. An alternative could be regular DFS or BFS, but they are more expensive.
'''

#  corridor  走廊