# encoding=utf-8
'''
draw the skyline
一堆interval，带有start和end，以及高度，整合之后， 请输出每个时间段及这个时
间段内最大的高度。

Example Input：
S1: {[2,5], vol=10}, {[6,10], vol=2}
S2: {[1,6], vol=1}, {[8,12], vol=8}

Example Output:
[1,2],vol=1, [2,5], vol=10, [5,6], vol = 1, [6,8], vol = 2, [8,12], vol = 8.

 {[2,5], vol=10}
rectangle(2, 5, 10)


http://www.mitbbs.com/article_t/JobHunting/32809753.html
'''
class Solution:
    def printSkyline(self, rects):
        points = {}
        pointsList = []
        pass
