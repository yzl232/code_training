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
#G家非常高频
#有障碍BFS。  没障碍求x,y 的median就可以。
# 实际上G家考的都是有障碍的。 也就是用k次BFS
'''
complexity k*n^2

k次BFS。求和就是得出了总距离矩阵。  每次都是独立的。


迷宫寻宝。一个grid表示的地图，上面有宝物，有障碍，要求找出图上一个点到所有宝物的总距离最短。



有一个gym，用block表示。里面有健身器材，还有障碍物。让找一个最佳的位 置放置椅子，使得椅子到所有健身器材的曼哈顿距离最短

    xxxx
  *x    x *
    xxxx
对于这个例子。  还是bfs最好吧~~

'''





#有障碍。 用BFS
#简单版本在这里   matrix_guard_barrier_保安_障碍
# global 的count矩阵。
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []: return
        m = len(board); n = len(board[0])  #因为最后结果cnt肯定不为0 。  所以还好
        cnt = [[0 if board[i][j]=='0' else None for j in range(n)] for i in range(m)]  # global 的count矩阵。   只对‘0’ 存数字
        for i in range(m):
            for j in range(n):
                if board[i][j]=='G':
                    tmpCntMatrix = self.bfs(board.copy(), i, j)
                    for x in range(m):
                        for y in range(n):
                            if tmpCntMatrix[x][y]!=None and cnt[x][y]!=None:
                                cnt[x][y]+=tmpCntMatrix[x][y]
        # find min in cnt that is big than 0

    def bfs(self, board, x, y):
        m = len(board); n = len(board[0])
        cntMatrix =  [[None for j in range(n)] for i in range(m)]
        cnt = 0; pre=[(x, y)]; board[x][y] = '#'; cnt[x][y]=0
        while pre:
            cur = set([]);  cnt+=1
            for i, j in pre:
                for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0<=r<=m-1 and 0<=c<=n-1 and board[r][c]=='0':
                        cur.add((r, c));   board[r][c] = '#'
                        if cntMatrix==None: cntMatrix[r][c]=cnt  #只考虑第一次过去
            pre = cur
        return cntMatrix
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
class Solution:
    def minTotalDistance(self, grid):
        x = [i for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]]
        y = [j for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j]]
        return sum(abs(x[len(x)/2]-i)+abs(y[len(y)/2]-j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j])

#这里的距离采用曼哈顿距离——|x0-x1| + |y0-y1|
#因为采用曼哈顿距离，所以可以分开考虑x坐标和y坐标。将k个点的x坐标排序，可以知道要求的x坐标一定在这k个点的x坐标上，

#实际上是取x坐标的中位数。   需要排好序。   默认就是排序的。
# 。对y坐标做同样的操作，从而得到答案。时间复杂度O(klogk)，排序的复杂度。
#  不需要什么quick select算法。 天生sort好了，    length/2就是median。      。 基于qiuck select的方法找median可以吧
#非常快。  用O(k)就可以了。 比O(k*n^2). 当然，也可以提一下。加分。
'''
On a given axis, the medium meeting place will
yield the shortest combined distance because if you go either direction by 1
from the medium, half of the people will travel 1 less block, and half plus
one people will travel 1 more block (For even number of people, any point
between the two middle will yield optimal result)
'''



#如果要求这个点与所给的k个点不重合，该怎么办？
'''
进阶：通过初阶的算法得到一个最优位置，如果这个位置与k个点重合，则从这个位置开始进行搜索，将这个点周围的点和对应的距离放入到一个堆里，每次从堆中取出最小距离的点，然后将这个点周围的点放入堆中，直到取出的点不与所给k个点重合。时间复杂度klogk，因为最多从堆中取出k+1个点即可找到一个不与所给k个点重合的点。堆每次操作为logk。
# 从最优位置开始BFS。 找第一个不重合的点。


'''
pass
'''
本题的最优算法较难想到。所以如果公司要求不高，答出O(nm)的方法即可。O(nm)的方法是因为假设我们知道在(x,y)这个位置的距离和为S，那么当(x,y)移动到(x+1,y)和(x,y+1)的时候，我们可以在O(1)的时间更新S。方法是预处理每一行上方/下方有多少个k个点中的点，每一列左侧/右侧有多少个k个点中的点。上面的解答基于nm>>klogk，如果k比较大，则还是O(nm)的方法更好。答题时需要答出对于给定参数不同情况下采用不用算法这一点。
'''




'''
Meeting place. You have a city with streets running parallel both
horizonally and vetically creating a giant grid. The dimension of each grid
is 1 X 1. All street corners in the city can be represented by a coordinate
(int x, int y).

 Given an array of people represented by their closest street
corner, calculate a street corner to meet where their combined traveling
distance is the shortest.

Assume everyone can only travel on road. For
example, the traveling distance from [1,1] to [2,2] is 2.


G家超高频。

4. Again, the key is to understanding how to minimize the combined distance
travelled.

 First of all, since you have to travel on the grid, x and y axis
are completely independent.

On a given axis, the medium meeting place will
yield the shortest combined distance because if you go either direction by 1
from the medium, half of the people will travel 1 less block,

 and half plus
one people will travel 1 more block (For even number of people, any point
between the two middle will yield optimal result).

In terms of
implementation, I'm not aware of a way to calculate the medium that's better
than O(N logN) which you can get by sorting (this is your opportunity to
shire with your sorting knowledge).


# median
'''