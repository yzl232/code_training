# encoding=utf-8
'''
There are N objects kept in a row. The ith object is at position x_i. You want to partition them into K groups. You want to move all objects belonging to the same group to the same position. Objects in two different groups may be placed at the same position. What is the minimum total amount by which you need to move the objects to accomplish this?

Input:
The first line contains the number of test cases T. T test cases follow. The first line contains N and K. The next line contains N space seperated integers, denoting the original positions x_i of the objects.

Output:
Output T lines, containing the total minimum amount by which the objects should be moved.

Constraints:
1 <= T <= 1000
1 <= K <= N <= 200
0 <= x_i <= 1000

Sample Input:
3

3 3
1 1 3

3 2
1 2 4

4 2
1 2 5 7

Sample Output:
0
1
3

Explanation:

For the first case, there is no need to move any object.
For the second case, group objects 1 and 2 together by moving the first object to position 2.
For the third case, group objects 1 and 2 together by moving the first object to position 2 and group objects 3 and 4 together by moving object 3 to position 7. Thus the answer is 1 + 2 = 3.




值。同时也是位置。    就是类似于clustering的问题。



Same DP approach as kkr.ashish above:
F(n+1,k) = min(F(n,k-1), F(n-1,k-1)+dist(a(n),a(n+1)), F(n-2,k-1)+dist(a(n+1),a(n),a(n-1)).............

where dist(a(n),a(n+1)..........) represents the minimum distance to group a(n),a(n+1)... into a partition.

Overall complexity is O(k*n^3) since each dist() takes O(n).


'''

#太难。 明显不会考的。 封存


class Solution:
    def minMoves(self, arr, k):
        n = len(arr);
        dp = [[10**10 for j in range(k) ] for end in range(n)]
        for end in range(n):  # arr[:end]
            dp[end][0] = self.minDist(arr, 0, end-1)    #分为1个group
        for end in range(n):
            for j in range(1, k):  #就是说k个group  =  k-1个group+ min_distance.    start 之前的k-1group, start之后一个group
                dp[end][j] = min(dp[start-1][j-1]+self.minDist(arr, start, end)  for start in range(j-1, end+1))
        return dp[-1][-1]
#we can precompute the distances for every pair of index at the start
    def minDist(self, arr, start, end):    #简单说，就是group到一个位置。求最小值。
        minDist = 0
        for i in range(start+1, end+1):  #全部group到start的位置。
            minDist +=arr[i]-arr[start]
        prevDist = minDist
        for i in range(start+1, end+1):
            dist = prevDist
            diff = arr[i]-arr[i-1]         #diff肯定>0
            dist += (i-start) * diff      #本身是sort得。  左边的变多了。 右边的变少了。
            dist -= (end-i+1) * diff
            minDist = min(minDist, dist)
            prevDist = dist
        return minDist