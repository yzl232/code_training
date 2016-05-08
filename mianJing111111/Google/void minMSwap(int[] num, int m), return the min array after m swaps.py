# encoding=utf-8
'''
void minMSwap(int[] num, int m), return the min array after m swaps

以前版里贴过的一题
void minMSwap(int[] num, int m), return the min array after m swaps， each
swap happens only between two adjacent elements([4,2,1,3], 2 return [1,4,2,3
] )
4,2,1,3
4,1,2,3
1,4,2,3

当时贴的解法是找最小的元素，判断swap它需要的最少交换次数n，
如果n<=m，swap过来，m -= n,递归，
如果n>m?那就找次小的，
重复上面的步骤

min = (m, len(arr))
在start到min得范围内找最小的。

'''

#和冒泡排序像。 O(n2)
class Solution:
    def minMSwap(self, arr, x):
        minArr = sorted(arr);  l=0
        while x>0 and arr!=minArr:
            r = x+l+1
            minV=min(arr[l:r]); minIdx = arr[l:r].index(minV)
            arr[l], arr[l+1:minIdx+1] = arr[minIdx], arr[l:minIdx]
            x-=minIdx-l;  l+=1
        return arr
s = Solution()
print s.minMSwap([4, 2, 1, 3], 2)

'''
class Solution:
    def minMSwap(self, arr, m):
        self.minArr = sorted(arr)
        self.dfs(0, m, arr)
        return arr

    def dfs(self, l, m, arr):
        if m==0 or arr==self.minArr : return
        r = min(m+l+1, len(arr))  #右边界比较赞
        minV=min(arr[l:r]);  minIdx = arr[l:r].index(minV)
        arr[l+1:minIdx+1], arr[l] = arr[l:minIdx], arr[minIdx]   #右移一位。
        self.dfs(l+1, m-(minIdx-l))
'''
'''
        minIdx = l;  r = min(m+l+1, len(self.arr))  #右边界比较赞
        for i in range(l, r):
            if self.arr[i]<self.arr[minIdx]:  minIdx=i
'''
