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

class Solution:
    def getCountTriangles(self, arr):
        n = len(arr)
        if n<3: return
        arr.sort()
        totalCount = 0;  curMaxPos = n-1
        while curMaxPos>=2:
            start=0; end = curMaxPos-1
            while start<end:
                if arr[start] + arr[end] <=arr[curMaxPos]:
                    start+=1
                else:
                    totalCount+= (end-start) #end固定了。 看start的种类
                    end-=1
            curMaxPos-=1
        return totalCount

#比较巧妙。
s = Solution()
print s.getCountTriangles([10, 21, 22, 100, 101, 200, 300])