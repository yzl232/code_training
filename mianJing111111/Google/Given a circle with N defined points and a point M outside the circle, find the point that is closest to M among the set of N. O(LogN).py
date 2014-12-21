# encoding=utf-8
'''
Given a circle with N defined points and a point M outside the circle, find the point that is closest to M among the set of N. O(LogN)
'''
#我们就先假定是sorted的吧。
#
'''


Assuming that the points on the circumference of the circle are "in-order" (i.e. sorted by angle about the circle's center) you could use an angle-based binary search, which should achieve the O(log(n)) bounds.

    Calculate the angle A from the point M to the center of the circle - O(1).
    Use binary search to find the point I on the circumference with largest angle less than A - O(log(n)).
    Since circles are convex the closest point to M is either I or I+1. Calculate distance to both and take the minimum - O(1).


'''

# 就是比较的时候，用角度比较。 寻找最接近的。 然后。 return min (arr[i], arr[i+1])


#大概是这样子做。 具体还得看具体的order的情况

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

    def search(self, x, arr):
        zero = (0, 0)
        l=0;  h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            c = self.orient(zero, x, arr[m])
            if c==0: return arr[m]
            elif c>0:  l=m+1
            else: h=m-1
        c1 = self.cross(zero, x, arr[l])
        c2 = self.cross(zero, x, arr[h])
        if abs(c1)>abs(c2): return l
        else: return h