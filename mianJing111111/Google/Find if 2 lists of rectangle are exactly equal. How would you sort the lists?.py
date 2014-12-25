# encoding=utf-8
'''
Find if 2 lists of rectangle are exactly equal. How would you sort the lists?
'''



#矩形可以用2个点表示。
'''
Imagine a rectangle represented as a ordered pair of 2 points. One on the upper left and the other on the lower right. Define a weak ordering comparator function first on the point (check if p1.x < p2.x and then p1.y < p2.y), then on the rectangle overall.

Now you can sort the two lists and check if they are the same.

Complexity O(n log n).

(Based on the assumption from the second part of your question, that is there is some well defined ordering on the rectangles : That is rectangles that start on a smaller x coordinate is "smaller")
'''
