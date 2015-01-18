# encoding=utf-8
'''
You are given an array, divide it into 2 equal halves such that the sum of those 2 halves are equal. (Imagine that such division is possible for the input array and array size is even)
'''

#我的想法是可以用dp值逆推




#dp
class Solution:
    def findPartition(self, arr):
        s = sum(arr); n=len(arr)
        if s%2!=0: return False  #i表示sum，  j表示arr
        s = s/2
        dp = [[False for i in range(n+1)] for j in range(s+1)]
        for i in range(n):   dp[0][i] = True     #sum 为0都是正确的
        for i in range(1, s+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1]  # exclude
                t = i-arr[j-1]   #
                if t>=0:   dp[i][j] = dp[i][j] or dp[t][j-1]
        if not dp[-1][-1]:  raise Exception('Can not be partitioned')
        i=s;  j=n  #由dp的值逆推的一个过程。 就是之前的反向
        exc=[]; inc=[]
        while i>0 and j>0:
            if dp[i][j] == dp[i][j-1] == True:
                exc.append(arr[j-1])
                j-=1
            else:
                inc.append(arr[j-1])
                j-=1; i-=arr[j-1]
        return exc, inc





#下面理解错了题意。

'''
给一个int[] array, e.g {1,5,0,6}和一个int target，e.g. target = 21;
问是否存在某种分法把array分成几部分，每部分看成一个int，这几部分加起来等于target。e.g. {1,5}{0}{6},三部分加起来是21。{1,5}{0,6}也是21。target=25则false

找到了k个不同的sum都是s/k。 成功

一个优化。 如果sum不是k的倍数。  return False

# np hard

以下优化
Sort the vector, v.
Eliminate elements bigger than k. They can't be part of any solution.




# 做法。 做k次  dfs。  每次dfs以后 ，  除去发现的sum为s/k的数
# 做k次 dfs。 （subset sum）

class Solution:
    def solve(self, arr, k):
        s = sum(arr)
        if s/k!=0: return False
        y = s/k;
        arr = [x for x in arr if x<=y]  #filter掉不合适的。
        for i in range(k):  pass
            # 做k次 dfs。  每次dfs后， remove掉， 再找。

    def dfs(self, arr, target):
        if target==0: return True
        if not arr: return False  #s不为0. 又为空。 False
        if arr[0]>target: return self.dfs(arr[1:], target)
        return self.dfs(arr[1:], target-arr[0]) or self.dfs(arr[1:], target)
'''