# encoding=utf-8
'''
给一个matrix，然后里面都是非负数，代表这一个点的高度。然后看这个matrix最大可以装多少水，和leetcode上的差不多，不过是二维的，要考虑上下左右。
'''



#bfs加上heap吧。

'''
For every point on the border set the water level to the point height
For every point not on the border set the water level to infinity
Put every point on the border into the set of active points
While the set of active points is not empty:
    Select the active point P with minimum level
    Remove P from the set of active points
    For every point Q adjacent to P:
        Level(Q) = max(Height(Q), min(Level(Q), Level(P)))
        If Level(Q) was changed:
            Add Q to the set of active points
'''