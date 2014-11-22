# encoding=utf-8
'''
Given the following 3 by 3 grid where the (first row, first column) is represented by (0,0):

0,  1 1   ,2 3,   3
1,    1 3,    3 3,   2
3,    0 1,     3 null

we need to find if we can get to each cell in the table by following the cell locations at the current cell we are at. We can only start at cell (0,0) and follow the cell locations from that cell, to the cell it indicates and keep on doing the same for every cell.


每个格子提供了某个坐标（a, b） 问我们是否能够遍历所有？？




Just like a graph traversal using a same size matrix with initial value set to -1. Mark the position you visited and, if you see a cycle (not -1 value), you know you will not be able to visit all the cells.

  找到了一个环。就退出。 然后check 是不是每个都visited的了。
  可以用hash。  O(m*n)


  可以用No extra space needed. change it to (-a, -b). In that case, we can revert it back after traverse.
  一旦发现了负数。 就退出循环。





用while循环。  一旦发现环。 停止。  遍历matrix。看是否都visit

'''