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
    def minMSwap(self, arr, m):
        self.arr2 = sorted(arr)
        if arr==self.arr2: return arr
        self.arr = arr
        self.dfs(0, m)
        return self.arr

    def dfs(self, start, m):
        if m==0 or self.arr==self.arr2 : return
        minI = start;  end = min(m+start+1, len(self.arr))
        for i in range(start, end):
            if self.arr[i]<self.arr[minI]:  minI=i
        self.arr[start+1:minI+1], self.arr[start] = self.arr[minI], self.arr[start:minI]
        self.dfs(start+1, m-(minI-start))