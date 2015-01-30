# encoding=utf-8
'''
然后问了一个数据存放的问题，如何在O(1)时间内取出一个matrix中间一个区域的数目之和，然后我之前看面经看过这个，然后用容斥原理做了，然后他说这是trade off，有办法能够平衡么？然后我就冒出来一个n个线段树的做法，取了平衡，他对我做法貌似挺满意的
'''


# 2-d  segment tee的做法更加平衡。    logN * logM.

# 容斥原理查询快。 更新慢。
'''


This is what Summed Area Tables are for. http://en.wikipedia.org/wiki/Summed_area_table

Your "preprocessing" step is to build a new matrix of the same size, where each entry is the sum of the sub-matrix to the upper-left of that entry. Any arbitrary sub-matrix sum can be calculated by looking up and mixing only 4 entries in the SAT.

EDIT: Here's an example.

For the initial matrix

0 1 4
2 3 2
1 2 7

The SAT is

0 1 5
2 6 12
3 9 22


#dp可以计算这个矩阵
The SAT is obtained using dp(x,y) = a(x,y) + S(x-1,y) + S(x,y-1) - S(x-1,y-1),

where S is the SAT matrix and a is the initial matrix .




If you want the sum of the lower-right 2x2 sub-matrix, the answer would be 22 + 0 - 3 - 5 = 14. Which is obviously the same as 3 + 2 + 2 + 7. Regardless of the size of the matrix, the sum of a sub matrix can be found in 4 lookups and 3 arithmetic ops. Building the SAT is O(n), similarly requiring only 4 lookups and 3 math ops per cell.


使用方法。容斥原理

x = dp[x+a][y+b]- (dp[x+a][y]+dp[x][y+b]-dp[x][y])

'''





'''

Given a 2D space of maximum size NxN which supports two operations :
     [1] void UPDATE(x,y,v) - sets the value of cell [x,y] to v
     [2] int QUERY(x1,y1,x2,y2) - returns sub-rectangle sum (x1,y1) to (x2,
y2)
      inclusive, and there is an infinite stream of such 2 types of
operations which have to supported. How would you store the values for
efficient updates and retrievals ?


你的方法对于query很有效。但是对update不够高效。可能要把整个matrix遍历一遍来
update。

【 在 ParanoidPark (ParanoidPark) 的大作中提到: 】
: 这个不就是用integral image
: 先建一个NxN的pre-sum数组，然后这个数组的(i,j)元素存的是从(0, 0)到(i, j)的
: subarray的和，
: 这样每次query任意sub-array的和，只用取出对应这个pre-sum数组的四个顶点的值
: A -----B
: |           |
: |           |
: C-----D
: 然后计算A+D-B-C就行了,这样query就是O(1).
'''



#G考过几次。 容斥原理
'''
1. 给一个矩阵A，要求输出一个矩阵B，要求B[i,j]=sum(A[l,k]) l<=i,k<=j;
例如 A=[1,1,2;
             0,3,1;
             2,1,0]
         B=[1,2,4;
               1,5,8;
               3,8,13];
follow up: 1.时间复杂度+如何测试
                2. 给定矩形块的upperx,uppery,lowerx,lowery，求矩形块的面积
                3. 如果 要多次运行函数求矩形块的面积，如何提高效率
'''