# encoding=utf-8
'''
Given a huge N*N matrix, we need to query the GCD of numbers in any given submatrix range（x1,y1,x2,y2）. Design a way to preprocess the matrix to accelerate the query speed. extra space should be less than O(N^2) and the preprocess time complexity should be as litte as possible.
'''
# logN * logM
#太过分了 用二维线段树。  还碰到了好几次。。。
'''
For each row A[i] in the matrix A, we build a segment tree.The tree allows us to query GCD(A[i][a..b]) 第i行第a到b列（不包括b)的最大公约数in O(log n) time . The memory complexity of each segment tree is O(n), which gives us O(n^2) total memory complexity.
时间复杂度，O(n2)建立线段树， log(N) log(M)查找，其中r and c are the number of rows and columns in the query.


<NM, log(N) log(M)>

This is just a 2D segment tree.  Break the rows up into segments as you would in the 1D case except their associated values are another segment tree on the columns.  This takes O(NM) memory and time to preprocess with O(log(N) log(M)) time to query.  This approach has an advantage over the following approaches in that it's dynamic; you can modify the values of the matrix in O(log(N) log(M)) time as well.
'''






#好几道G家这种题目
'''
You are given the toplogical information of a terrain in the following format - There are n points ( x_i , y_i ) and for each point (x_i , y_i ) the altitude h_i is given.

For any rectangle (axis parallel) defined by the x-y coordinates of
the corner points, we must answer the query about which is the highest altitude point lying within the rectangle.

Implement this using a range-query data-structure that answers such a
query in O( log^2 n) time
'''


'''
This can be done using a 2-D segment tree.
The first segment tree will be for representing the range on the x-axis.
Now, for each node(range) in this segment tree, there will be a segment tree representing the y-ranges.
So, lets say we get a query xi,yi to xf,yf(representing diagonal points of the rectangle). , we first travel in the first segment tree for the range xi to xf. Then for that node, we take we search for the range yi to yf in the corresponding tree for xi to xf.

Time complexity- for building the tree= (xrange*yrange), for each query= (log(xrange)*log(yrange))

space complexity= xrange*yrange. (since we store a segment tree in an array. In this case 2-D array. ) Each node in the array for first segment tree will contain pointer to the array for this 2-D array.
'''