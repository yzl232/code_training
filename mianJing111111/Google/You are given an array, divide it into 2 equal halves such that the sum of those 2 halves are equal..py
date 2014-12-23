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