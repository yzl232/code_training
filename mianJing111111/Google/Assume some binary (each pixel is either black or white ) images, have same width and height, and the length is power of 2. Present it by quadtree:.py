# encoding=utf-8
'''
Assume some binary (each pixel is either black or white ) images, have same
width and height, and the length is power of 2. Present it by quadtree:
divide the image into quarters, each quarter can be all back, all white or
mixed, subdivide the mixed ones… recurse.

#四叉树。。。
'''

#考过好几次。
'''
比如一个二维的 image, 里面的 pixel是 白或者黑,  若果所有的pixel是黑
那么这个 image就是黑(B)的，如果所有的pixel 是白(W)的，那么这个 image就是白的。
否则的话，需要把这个 image等分成四份，如下图

__________                     __________
|        |   等分成四份就变成  |    |   |
|        |                     |____|___|
|        |                     |    |   |
|________|                     |____|___|

分成四份以后每个小份就是一个  sub-quadtree

问题1 : 为这个 quadtree里面的 node 设计 data structure

然后的问题是关于两个 quadtree 的 intersection, 有两个 quadtree, 它们描述的
image 是两个相同的 area
比如 都是 [0 1] x [0 1] 这个相同的二维区域的image.

问题二: 写一个函数，返回两个 quadtree的intersection,

这个intersection的规则是: 如果一个区域在 第一个quadtree 里面是
白的，这个相同的区域在 第二个 quadtree里面是黑的，那么intersection
就是白的，简单的说白是 0, 黑是 1, intersection就是两个bit 的 AND
'''

#https://www.youtube.com/watch?v=S-SnhregzOI

#  https://www.youtube.com/watch?v=dwlRvmONZNU
#http://tech.ddvip.com/2013-10/1382720289204853.html
#a) how to present this image
class QuadTree:
    def __init__(self,  size, color = 'black',):
        self.nw =  self.ne = self.se = self.sw=None
        self.color = color
        self.size = size

#b) count all the black pixels of this image
class Solution:
    def cntB(self, root, depth, size):
        if not root:   return 0     #混合的话。 就是color = "mixed"
        if root.color == "white":    return 0
        elif root.color == "black":    return  root.size**2
        else:   return self.cntB(root.se)+ self.cntB(root.sw)+ self.cntB(root.ne)+ self.cntB(root.nw)

#(c ) merge two image( actually it's to "and" two image with same size since
#all pixels are boolean)
#实际上就是求和

class Solution5:
    def merge(self, root1, root2):
        assert  root1.size == root2.size  #assert比raise value error更加简短
        if not root1 or not root2: return
        if root1.color or root2.color =='mixed':
            root = QuadTree('mixed', root1.size)
            root.ne = self.merge(root1.ne, root2.ne)
            root.nw = self.merge(root1.nw, root2.nw)
            root.se = self.merge(root1.se, root2.se)
            root.sw = self.merge(root1.sw, root2.sw)
        elif root1.color == root2.color =='white':  return QuadTree('white', root1.size)
        else: return QuadTree('Black', root1.size)