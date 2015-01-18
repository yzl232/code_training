# encoding=utf-8
'''
Given the relative positions (S, W, N, E, SW, NW, SE, NE) of some pairs of points on a 2D plane, determine whether it is possible. No two points have the same coordinates.
e.g., if the input is "p1 SE p2, p2 SE p3, p3 SE p1", output "impossible".
'''

# build 2 graphs。    x,  cooridinates.  y  coordinates

'''
One idea, not sure whether this is correct.

Construct two graphs, one for x-coordinate--Gx, one for y-coordinate--Gy.

For Gx, If x1 < x2, then we have an edge from x1->x2, if x1 > x2, one edge x1<-x2. If x1 == x2, combine x1 and x2 together.

Similarly for Gy.

In the end, we check whether there exists a cycle in Gx or Gy. If this is true, then the answer is impossible.

For example, p1 SE p2, we have x1 > x2 and y1 < y2.
Gx: x1 <-- x2 Gy: y1 -->y2

p2 SE p3, we have x2 > x3 and y2 < y3.
Gx: x1 <-- x2 <-- x3 Gy: y1 -->y2 -->y3

p3 SE p1, we have x3 > x1 and y3 < y1
In Gx, we have a cycle from x1 <-- x2 <-- x3 <-- x1. So it is impossible.
'''