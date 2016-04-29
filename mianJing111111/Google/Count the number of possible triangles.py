# encoding=utf-8
'''


Count the number of possible triangles

Given an unsorted array of positive integers. Find the number of triangles that can be formed with three different array elements as three sides of triangles. For a triangle to be possible from 3 values, the sum of any two values (or sides) must be greater than the third value (or third side).
For example, if the input array is {4, 6, 3, 7}, the output should be 3. There are three triangles possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}. Note that {3, 4, 7} is not a possible triangle.
As another example, consider the array {10, 21, 22, 100, 101, 200, 300}. There can be 6 possible triangles: {10, 21, 22}, {21, 100, 101}, {22, 100, 101}, {10, 100, 101}, {100, 101, 200} and {101, 200, 300}


Method 1 (Brute force)
The brute force method is to run three loops and keep track of the number of triangles possible so far. The three loops select three different values from array, the innermost loop checks for the triangle property ( the sum of any two sides must be greater than the value of third side).

Time Complexity: O(N^3) where N is the size of input array.

暴力法： cube.
优化:第一： sort.  只要考虑最小的两边，和大于第三边就好。
然后就是固定最大的边。 然后用2个指针搜索就好了。
start, end.
最开始end固定。 增大start， 看start有多少种
然后end-1,  继续。看start多少种。
'''
#一个for 循环。一个while， 就是 3 sum的变体
#实质上是3sum
#不是G家。 但是很像的那道是G家。


class Solution:
    def getCountTriangles(self, arr):
        if len(arr)<3: return 0
        cnt=0; arr.sort()
        for big in range(len(arr)-1, 1, -1):
            l=0; r=big-1
            while l<r:
                if arr[l]+arr[r]<=arr[big]: l+=1
                else:
                    cnt+=r-l
                    r-=1
        return cnt


#比较巧妙。
s = Solution()
print s.getCountTriangles([10, 21, 22, 100, 101, 200, 300])
#和那个count  平方数目的也很像
#Count Distinct Non-Negative Integer Pairs (x, y) that Satisfy the Inequality。。。
# Let's say there is a double square number X
# 类似这题 Input - array of integers size N, integer Threshold