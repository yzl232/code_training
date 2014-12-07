# encoding=utf-8
'''

How to check if two given line segments intersect?

Given two line segments (p1, q1) and (p2, q2), find if the given line segments intersect with each other.

Before we discuss solution, let us define notion of orientation. Orientation of an ordered triplet of points in the plane can be
–counterclockwise
–clockwise
–colinear
The following diagram shows different possible orientations of (a, b, c)

'''


'''
// To find orientation of ordered triplet (p, q, r).
// The function returns following values
// 0 --> p, q and r are colinear
// 1 --> Clockwise
// 2 --> Counterclockwise


Here orientation is nothing but the cross product.
Orientation (p,q,r ) is cross product of Vector(p to q ) and Vector( p to r ).



点乘
ab旋转到ac. 如果是clockwise的角度更近。 就是正。 否则负数

         b
a           c
正
              c
a        b
负


clock wise的方向。 正
θ has a slightly different meaning in this case: |θ| is the angle between the two vectors, but θ is negative or positive based on the right-hand rule. In 2-D geometry this means that if A is less than 180 degrees clockwise from B, the value is positive
'''




class Solution:
    def orient(self, p, q, r):
        c = self.cross(p, q, r)
        if c==0: return 0
        elif c>1: return 1
        else: return -1

    def cross(self, a, b, c):
        ab = [b[0]-a[0], b[1]-a[1]]
        ac = [c[0]-a[0], c[1]-a[1]]
        return ab[0]*ac[1]-ab[1]*ac[0]

    def doIntersect(self, p1, p2, q1, q2):
        o1 = self.orient(p1, p2, q1)
        o2 = self.orient(p1, p2,q2)
        o3 = self.orient(q1, q2, p1)
        o4 = self.orient(q1, q2, p2)
        if o1!=o2 and o3!=o4: return True  #general case  方向不同的时候，一定相交。  包含了所有不在同一直线的case。
        #特殊情况。这里只是同一直线的情况。(colinear)
        if o1==0 and self.onSegment(p1, p2, q1): return True  #special cases
        if o2==0 and self.onSegment(p1, p2,q2): return True
        if o3==0 and self.onSegment(q1, q2, p1): return True
        if o4==0 and self.onSegment(q1, q2, p2): return True
        return False

#点q在线段pr上。
    def onSegment(self, p1,p2, q):
        if min(p1[0], p2[0])<=q[0]<=max(p1[0], p2[0])  and  min(p1[1], p2[1])<=q[1]<=max(p1[1], p2[1]): return True
        return False