# encoding=utf-8
'''
Given a polygon and a point ‘p’, find if ‘p’ lies inside the polygon or not. The points lying on the border are considered inside.


有进有出。 如果只有一次。
在外面。一定是有进有出。
在里面，只有出去一次。

Following is a simple idea to check whether a point is inside or outside.

1) Draw a horizontal line to the right of each point and extend it to infinity

1) Count the number of times the line intersects with polygon edges.

2) A point is inside the polygon if either count of intersections is odd or
   point lies on an edge of polygon.  If none of the conditions is true, then
   point lies outside.
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

    def isInswide(self, polygon, p):
        if len(polygon)<3: return False
        bigX = max(t[0] for t in polygon)+1   #善用list comprehension。很牛逼。
        extreme = [bigX, p[1]]; count = 0
        for i in range(len(polygon)):
            nextP = (i+1)%len(polygon)
            if self.orient(polygon[i], polygon[nextP], p)==0 and self.onSegment(polygon[i],polygon[nextP], p):   return True
            if self.doIntersect(polygon[i], polygon[nextP], p, extreme): count+=1
        return  count%2==1