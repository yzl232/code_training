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
def overLap(l1, r1, l2, r2):
    if l1.x>r2.x or l2.x>r1.x:  return False #1， 2互换一下
    if l1.y<r2.y or l2.y<r1.y: return False
    return True