# encoding=utf-8
'''
Given a polygon with N vertexes and N edges. There is an int number(could be negative) on every vertex and an operation in set(*,+) on every edge. Every time, we remove an edge E from the polygon, merge the two vertexes linked by the edge(V1,V2) to a new vertex with value: V1 op(E) V2. The last case would be two vertexes with two edges, the result is the bigger one.
Return the max result value can be gotten from a given polygon.
'''




#一看是多边形就会难。

'''
A variation of the matrix chain multiplication should work.
Let the number at each vertex and the (clockwise) next edge be a single element....

struct element {
      int num;
      char op;
}pol[N];

Initialize a 2D matrix m[NxN]

Let m[i,i] = pol[i] for 1 <= i <= N

Let m[i,j] be the maximum value that can be achieved from the subset of elements from index i to index j.

Using the recursive equation :
m[i,j] = max { m[i,k] [operation for element at index k] m[k+1,j] } :: for 1 <= i <= k <= j <= N

This would give the maximum value if the list was linear, but since it is a circular linked list, repeat the entire procedure for the different start points in the circular linked list.
'''

#pass

'''
this makes sense. I wrote some code to elaborate the idea. let me know if I get it right. time complexcity O(n^3)

assume input as two arrays: list[N] has N integers, operator[N] has N corresponding operators

int dp[][]=new int[N][N]; /* row i represents computing with starting point of list[i] and column j represents the max result with j numbers after list[i];*/

int max=Integer.MIN_VALUE;

for(int i=0;i<N;i++){
dp[i][0]=list[i];}

for(int j=1;j<N;j++){
for(int i=0;i<N;i++){
for(int k=0;k<j;k++){

int val=compute(dp[i][k],operator[(i+k)%N],dp[(i+k+1)%N][j-k-1]);

if(val>dp[i][j]) dp[i][j]=val;
if(val>max&&j==N-1) max=val;
}}}

return max;
'''


class Solution:
    def distance(self, a, b):
        return (b[0]-a[0])**2+(b[1]-a[1])**2

    def compute(self, x1, x2, op):
        if op=='*': return x1*x2
        elif op=='+': return x1+x2

    def solve(self, arr, ops):
        n = len(arr);  ret = 0
        dp  =[[0]*n for i in range(n)]
        for i in range(n):  dp[i][i] = arr[i]  # length 为0
        for length in range(1, n):
            for i in range(n):
                j = (i+length)%n
                dp[i][j] = max(self.compute(  dp[i][k%n], dp[k%n+1][j], ops[k%n])  for k in range(i+1, i+length))  #compute代表最后一次运算
                if length==n-1: ret =max(ret, dp[i][j])
        return ret
#和triangulation   那道题目基本上一样了。 不同在于这里比较关心circular.   于是加上了%n
