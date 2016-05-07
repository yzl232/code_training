# encoding=utf-8
'''
Given an array of integer where a means a link from i => a. You need to return the length of longest cycle formed by these links.

 There are two cycles. The first is [1,2,0], and the second is [3]. So the length of the longest cycle is 3.

 [1,2,0,3]

 Notice: There could be duplicated values in the array.
Your algorithm needs to run no worse than O(n) time where n is the size of the array.
'''

'''
如果数组元素不在[0..n - 1]我们认为是断裂，即无法走到下一个节点。
如果没有断裂，一定有圈。
'''
# http://www.meetqun.com/forum.php?mod=viewthread&tid=2518&fromuid=12
# 我们只要走到一个走过的节点或者断裂，就可以停止本次找寻
#  结束时如果停止的节点时本轮里经过的，我们就找到一个圈。 比如1->2->3->4->2 。
class Solution:  # time stamp
    def solve(self, arr):  #
        n = len(arr); time=0; ret=0; d = {}
        for i in range(n):
            if i not in d:
                x=i
                while 0<=x<n and x not in d:
                    d[x]=time;  time+=1;   x = arr[x]
                if 0<=x<n and d[x]>=d[i]:   ret=max(ret, time-d[x])   # ts[x]>=ts[i]代表是本轮循环。
        return ret  #x是交叉点， i是起始点，  如果交叉点小于起始点， 那么是以前的cycle.
# ts[x]<ts[i], 代表是以前visited，跳过。ts[x]==ts[i]代表正好起点也在环内。  ts[x]>ts[i]起点不在环内

s = Solution()
print s.solve([2, 2, 1])
print s.solve([1, 2, 0])