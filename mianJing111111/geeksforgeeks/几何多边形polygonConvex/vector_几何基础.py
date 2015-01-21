# encoding=utf-8
'''
 补上几何基础

 vector    两点差： the line segment from (1,3) to (5,1) can be represented by the vector (4,-2).
 dot production:     结果是一个数。   dot product of (x1, y1) and (x2, y2) is x1*x2 + y1*y2.

特别适合用来计算A ⋅ B = |A||B|Cos(θ)
cos的值。



 The cross product of two 2-D vectors is
 x1*y2 - y1*x2

 A x B =
  | x1   x2    |
  | y1   y2    |

  =   x1*y2 - y1*x2

  u=(1,2) and v=(3,4)

  So the determinant of your 2x2 is just
(1*4) - (2*3)
------------------
For a more visual explanation:

matrix:
u = (a, b)
v = (c, d)

determinant: ad - bc

方向是z轴。  管不到三维。忽略之。
  A x B = |A||B|Sin(θ).

  用来计算sin
可以用来求面积。
  Line-Point Distance
  用sin
  3 points, A, B, and C,
  (AB x AC)/|AB|.
'''

'''

'''


class VectorOperations:
    def dot(self, a, b, c):
        ab = [b[0]-a[0], b[1]-a[1]]
        ac = [c[0]-a[0], c[1]-a[1]]
        return ab[0]*ac[0]+ab[1]*ac[1]
        #  return (b[0]-a[0])*(c[0]-a[0])+(b[1]-a[1])*(c[1]-a[1])

# AB x AC  注意我这里没有写AB X BC
    def cross(self, a, b, c):
        ab = [b[0]-a[0], b[1]-a[1]]
        ac = [c[0]-a[0], c[1]-a[1]]
        return ab[0]*ac[1]-ab[1]*ac[0]
#点乘用来判断锐角，钝角。  叉乘可以判断orientation，三角形面积。  都非常有用。
    def distance(self, a, b):
        return (b[0]-a[0])**2+(b[1]-a[1])**2

    def linePointDistance(self, a, b, c, isSegment):
        dis = 1.0*self.cross(a, b, c)/self.distance(a, b)
        if isSegment:
            dot1 = self.dot(b, a, c)  #a, b, c大于90度
            if dot1<=0: return self.distance(b, c)  #b, c 2点的距离
            dot2 = self.dot(a, b, c)  #b, a, c 大于90度
            if dot2<=0: return self.distance(a, c) #a, c   2点距离。  大于90度
        return dis

    def polygonArea(self, p):  #求多边形面积。牛逼。
        return abs(sum(self.cross((p[0], p[i], p[i+1])) for i in range(1, len(p)-1)))/2.0  #只要求cross就可以了。几行代码

'''
                  b
    a                    c         b, c 2点的距离    大于90度


                     a
                            b      a, c   2点距离。  大于90度
    c

Consider the non-convex polygon below, with 5 points. To find its area we are going to start by triangulating it.
多边形面积。 第一步，分为三角形。

简单的说， 就是点乘的和。  正负它们会自动抵消。
'''

'''
cross product
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


