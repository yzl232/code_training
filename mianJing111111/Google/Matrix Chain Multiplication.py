# encoding=utf-8
'''
他翻了一下简历，发现对一个project有点兴趣，于是我们花了五分钟讨论了一下。然后是题，算法导论里面的矩阵相乘的题，然后用动态规划做出来了，写了代码，一起讨论了一下边缘问题，然后就到了两点半，发现这个room被预定了，后面的人也来了，于是面试就结束了。.
'''

'''
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

We have many options to multiply a chain of matrices because matrix multiplication is associative. In other words, no matter how we parenthesize the product, the result will be the same. For example, if we had four matrices A, B, C, and D, we would have:

    (ABC)D = (AB)(CD) = A(BCD) = ....

However, the order in which we parenthesize the product affects the number of simple arithmetic operations needed to compute the product, or the efficiency. For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix. Then,

    (AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
    A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.

'''

# O（n3）
class Solution:
    def solve(self, arr):  #n个矩阵。 n-1个不同维度。
        n =len(arr)
        assert n>=3
        dp = [[0]*n for i in range(n)]  #初始： dp[i][i]=0
        for j in range(n):
            for i in range(j-1, 0, -1):  #  极端例子。成立 。  # say  1 3  5 .     j=2.   i=1,
                dp[i][j] = min(dp[i][k]+dp[k+1][j]+ arr[i-1]*arr[k]*arr[j] for k in range(i, j))
        return dp[1][-1]    #注意是arr[i-1]起点相乘。 所以内循环不能达到arr[0]。  所以dp[1][-1]
#  1  2 3 4 3 代表 1x2 2x3  3x4  4x3  四个矩阵
# arr[i-1]*arr[k]*arr[j]  两个矩阵相乘，就是三个点。 i-1是之前没用过的。 k是中间。
s = Solution()
print s.solve([10 , 30 ,5, 60])
'''
or example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix. Then,

    (AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
    A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.

'''

# 两个矩阵相乘， 就是10*30*50
