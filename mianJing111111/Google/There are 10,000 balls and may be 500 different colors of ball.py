# encoding=utf-8
'''
There are 10,000 balls and may be 500 different colors of ball

Example: There are:

4 - red ball
5900 - Blue ball
3700 - Green ball
396 - mintcream ball
Or there may be 10,000 red balls.

Or all balls are has same range, i.e. 500 red, 500 blue, etc.

We don’t know the range of any ball and number of color balls, but the minimum is 1 color and maximum is 500 colors, and we have auxiliary array of size 500. how to arrange all same color ball together in minimum passes over balls? is it possible to do in less than two passes ??
'''


'''
arr[500]
for ball in balls:
  aux_array[ball.color].append(ball)
'''