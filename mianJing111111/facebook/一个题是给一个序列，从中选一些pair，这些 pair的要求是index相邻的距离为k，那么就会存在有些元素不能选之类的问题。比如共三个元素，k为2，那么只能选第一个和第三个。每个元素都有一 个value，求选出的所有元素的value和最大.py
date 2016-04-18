# encoding=utf-8
'''
一个题是给一个序列，从中选一些pair，这些 pair的要求是index相邻的距离至少为k，那么就会存在有些元素不能选之类的问题。比如共三个元素，k为2，那么只能选第一个和第三个。每个元素都有一 个value，
#选pair的和最大
'''

'''
一个题是给一个序列，从中选一些pair，这些 pair的要求是index相邻的距离为k，那么就会存在有些元素不能选之类的问题。

我想了一下。 不是求累积sum。 应当是辅助array。left max。  然后
ret = max(ret, arr[i]+leftMax(i-k))

可以做到one pass
'''

class Solution:
    def findPairt(self, arr, k):
        assert len(arr)>k
        dp = arr[:]
        ret = float('-inf')
        for i in range(len(arr)):
            dp[i] = max(dp[i-1], arr[i])
            if i-k>=0: ret = max(ret,  arr[i]+dp[i-k])
        return ret

s = Solution()
print s.findPairt([1,3, 5,2, 8, 3,6], 2)