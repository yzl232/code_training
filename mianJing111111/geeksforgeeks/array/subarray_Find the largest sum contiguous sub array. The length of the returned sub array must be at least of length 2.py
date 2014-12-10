# encoding=utf-8
'''
Find the largest sum contiguous sub array. The length of the returned sub array must be at least of length 2

这道题目挺难。 珍藏一下。
'''

'''
可以先写一下只取和的版本。   以此为基础。 可以写出求具体array的版本
'''
class Solution1:
    def maxSum2(self, a):
        if len(a)<2: return
        ret= maxN = a[0]+a[1]
        for i in range(2, len(a)):
            maxN = max(maxN+a[i], a[i-1]+a[i])
            ret = max(maxN, ret)
        return ret



#对比一下最普通的结果。
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, a):
        ret = maxN = a[0]
        for i in range(1, len(a)):
            maxN = max(maxN + a[i],  a[i])
            ret = max(ret, maxN)
        return ret


class Solution3:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, a):
        if len(a)<2: return
        result = [a[0]+a[1], 0, 1]
        maxEndingHere = [a[0]+a[1], 0, 1]
        for i in range(2, len(a)):
            if a[i]+a[i-1]>maxEndingHere[0]+a[i]:  #本质上还是这2个比较   以前是maxEndingHere+a[i] 比 a[i]。 现在时比a[i]+a[i-1]
                maxEndingHere = [a[i]+a[i-1], i-1, i]
            else:
                maxEndingHere[0] = maxEndingHere[0]+a[i]
                maxEndingHere[-1] = i
            if maxEndingHere[0] > result[0]:  #本质上还是这2个比较
                result = maxEndingHere
        return a[result[1]:result[2]+1]
s = Solution()
print s.maxSubArray([1,2,3,-7,1,1,2])
print s.maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3])