# encoding=utf-8
'''
We strongly recommend to see the following post first.
How to check if two given line segments intersect?

The idea of Jarvis’s Algorithm is simple, we start from the leftmost point (or point with minimum x coordinate value) and we keep wrapping points in counterclockwise direction. The big question is, given a point p as current point, how to find the next point in output? The idea is to use orientation() here. Next point is selected as the point that beats all other points at counterclockwise orientation, i.e., next point is q if for any other point r, we have “orientation(p, r, q) = counterclockwise”. Following is the detailed algorithm.

1) Initialize p as leftmost point.
2) Do following while we don’t come back to the first (or leftmost) point.
…..a) The next point q is the point such that the triplet (p, q, r) is counterclockwise for any other point r.
…..b) next[p] = q (Store q as next of p in the output convex hull).
…..c) p = q (Set p as q for next iteration).
'''
#2种解法都是geeksforgeeks上面的
#O(n2)
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

    def converxHull(self, points):
        n = len(points)
        if n<3: return
        next = {i:-1 for i in range(n)}
        l = min(points)   #下面必须用while 循环
        p = l
        while True:
            q = (p+1)%n
            for r in range(n):
                if self.orient(p, q, r)==-1:  q=r
            next[p] = q
            p = q
            if p==l: break
        for i in range(n):
            if next[i] !=-1:  print points[i]


'''
Overall complexity is O(n) + O(nLogn) + O(n) which is O(nLogn)
和Next Greater Element的方法很像。
'''
class Solution5:
    def orient(self, p, q, r):
        c = self.cross(p, q, r)
        if c==0: return 0
        elif c>1: return 1
        else: return -1

    def cross(self, a, b, c):
        ab = [b[0]-a[0], b[1]-a[1]]
        ac = [c[0]-a[0], c[1]-a[1]]
        return ab[0]*ac[1]-ab[1]*ac[0]

    def distance(self, a, b):
        return (b[0]-a[0])**2+(b[1]-a[1])**2

    def cmp(self, p1, p2):
        if p1==p2: return 0
        p = self.points[0]
        t = self.orient(p, p1, p2)
        if t==0: return 1 if self.distance(p, p1)>self.distance(p, p2) else -1
        return t

    def converxHull(self, points):
        yMin = points[0]; iMin = 0;  n=len(points)
        for i in range(1, len(points)):
            if points[i][1]<yMin:
                yMin = points[i][1]
                iMin = i
        points[0], points[iMin] = points[iMin], points[0]
        self.points = points
        points =points[:1]+ points[1:].sort(self.cmp)  #完成了排序了
        stack = [points[0], points[1], points[2]]
        for i in range(3, n):
            while len(stack)>=3 and self.orient(stack[-2], stack[-1], points[i])!=-1: stack.pop()
            stack.append(points[i])   #也就是不是左拐， 就要pop
        for x in stack:
            print x