# encoding=utf-8
'''


Find if two rectangles overlap

Given two rectangles, find if the given two rectangles overlap or not.

Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates.
l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.


'''

#只要2个点就可以表示一个矩形了。。。
#l代表左上, topleft。  r代表右下.  bottom right
# 一个是x坐标没重叠。 一个是y坐标不重叠。    再每次1， 2互换一下。  共4种
def overLap(p1L, p1R, p2L, p2R):
    if p1R.x<p2L.x or p2R.x<p1L.x:  return False   # 每次1， 2互换一下
    if p1R.y > p2L.y or p2R.y>p1L.y: return False
    return True