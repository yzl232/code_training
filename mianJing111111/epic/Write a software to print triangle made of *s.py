# encoding=utf-8
'''
Write a software to print triangle made of *s. Given the height and width of Triangles in terms of number of stars. like to output

*
* *
* * *

given you have to use 3 stars or the height is 3 stars.

稍微特别的三角形, 其实不是三角形。   第一行。 高0。  宽1， .     最后一行高h-1, 宽w。
求等差数列吧。  第一行为1.  最后一行为w

'''
class Solution:
    def pTriangle(self, h, w):
        result = [1]
        diffe = (w-1)*1.0/(h-1)
        for i in range(1, h):
            result +=[int(1+i*diffe)]
        for i in result:
            print '*' * i
        print

s = Solution()
s.pTriangle(3, 6)
s.pTriangle(3, 3)
s.pTriangle(3, 9)
s.pTriangle(5, 9)