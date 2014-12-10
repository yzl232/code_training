# encoding=utf-8
'''


Maximum circular subarray sum

Given n numbers (both +ve and -ve), arranged in a circle, fnd the maximum sum of consecutive number.

与leetcode拿到题目不同。这个事圆形。

Examples:

Input: a[] = {8, -8, 9, -9, 10, -11, 12}
Output: 22 (12 + 8 - 8 + 9 - 9 + 10)

Input: a[] = {10, -3, -4, 7, 6, 5, -4, -1}
Output:  23 (7 + 6 + 5 - 4 -1 + 10)

Input: a[] = {-1, 40, -14, 7, 6, 5, -4, -1}
Output: 52 (7 + 6 + 5 - 4 - 1 - 1 + 40)

case1:  subarray question
case2:  wrapping occurs.
#Wrapping of contributing elements implies non wrapping of non contributing elements

so find out the sum of non contributing elements and subtract this sum from the total sum. To find out the sum of non contributing, invert sign of each element and then run Kadane’s algorithm

Our array is like a ring and we have to eliminate the maximum continuous negative that implies maximum continuous positive in the inverted arrays.
那个东西反用就是求最小值了。 也就是会贡献负数的值。 sum, 去掉这部分贡献负数的值。就是circular结果了



'''


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, a):
        result = maxN = a[0]
        for i in range(1, len(a)):
            maxN = max(maxN + a[i],  a[i])
            result = max(result, maxN)
        return result

    def maxCircularSum(self, a):
        v1 = self.maxSubArray(a)  # sub
        v2 = sum(a)
        a = [-x for x in a]
        v2 +=self.maxSubArray(a)  #
        return max(v2, v1)

s = Solution()
print s.maxCircularSum([8, -8, 9, -9, 10, -11, 12])