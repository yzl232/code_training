# encoding=utf-8
'''
2d array ＊代表障碍物 ＃代表货物 空白就是正常的路
问
如何找到一个点为出发点 能实现总共取货路径最短？ 每次只能拿一个货物，遇到障碍
需要绕开，拿到以后要放回出发点，然后再取另一个

＊＊＊＊＊＊
＊   ＃       ＊
＊  ＊＊＊  ＊
＊              ＊
＊     ＊＊   ＊
＊ ＃       ＃＊
＊＊ ＊＊＊＊
'''


'''
find a intersection to build office so that the sum of all employees’
commute distances is minimum. （the map is represented as a m*n grid, you
are given each employee’s coordination, they can only move in up-down and
left-right directions）
'''



#因为每次要回到原点。 所以是独立的。
#找出那个点
#用障碍物，那只能用BFS。  没有障碍物，直接算曼哈顿距离。
'''
 bfs from every box. in each box , a non blocking cell(include box position
,
:  but exclude hazard position ) will have a weight value , stand for the
: distance to the box. after bfs from all the boxes , each cell will have k
: weight, k is the number of boxes. sum all the weight in each cell , and
find
:  the cell with smallest sum of weight. One problem of this solution may
lead
:  to a cell of a box. revision is sort the cell by sum of weight and find
the
:  first that is not a box.
: complexity k*n^2
'''


'''
在一个n*m的矩阵中，有k个点，求矩阵中距离这k个点的距离和最近的点
'''

#这里的距离采用曼哈顿距离——|x0-x1| + |y0-y1|
#因为采用曼哈顿距离，所以可以分开考虑x坐标和y坐标。将k个点的x坐标排序，可以知道要求的x坐标一定在这k个点的x坐标上，扫描一遍并统计到各个点的x坐标距离和，找到使得距离和最小的x坐标。这一步只需要O(k)的时间复杂度，而不是O(k^2)，怎么优化这里不多赘述。对y坐标做同样的操作，从而得到答案。时间复杂度O(klogk)，排序的复杂度。


#如果要求这个点与所给的k个点不重合，该怎么办？
'''
进阶：通过初阶的算法得到一个最优位置，如果这个位置与k个点重合，则从这个位置开始进行搜索，将这个点周围的点和对应的距离放入到一个堆里，每次从堆中取出最小距离的点，然后将这个点周围的点放入堆中，直到取出的点不与所给k个点重合。时间复杂度klogk，因为最多从堆中取出k+1个点即可找到一个不与所给k个点重合的点。堆每次操作为logk。



'''
pass
'''
本题的最优算法较难想到。所以如果公司要求不高，答出O(nm)的方法即可。O(nm)的方法是因为假设我们知道在(x,y)这个位置的距离和为S，那么当(x,y)移动到(x+1,y)和(x,y+1)的时候，我们可以在O(1)的时间更新S。方法是预处理每一行上方/下方有多少个k个点中的点，每一列左侧/右侧有多少个k个点中的点。上面的解答基于nm>>klogk，如果k比较大，则还是O(nm)的方法更好。答题时需要答出对于给定参数不同情况下采用不用算法这一点。
'''