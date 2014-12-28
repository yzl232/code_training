# encoding=utf-8
'''
You have k lists of sorted integers. Find the smallest range that includes at least one number from each of the k lists.

For example,
List 1: [4, 10, 15, 24, 26]
List 2: [0, 9, 12, 20]
List 3: [5, 18, 22, 30]

The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3.'''


#一看到多个sorted array就是 n-way merge。用min heap
#和facebook题像
## Find a minimum range contain a number from each row
'''
There are k lists of sorted integers. Make a min heap of size k containing 1 element from each list. Keep track of min and max element and calculate the range.
In min heap, minimum element is at top. Delete the minimum element and another element instead of that from the same list to which minimum element belong. Repeat the process till any one of the k list gets empty.
Keep track of minimum range.

For eg.
List 1: [4, 10, 15, 24, 26]
List 2: [0, 9, 12, 20]
List 3: [5, 18, 22, 30]

Min heap of size 3. containing 1 element of each list
Heap [0, 4, 5]
Range - 6

Remove 0 and add 9
Heap [4, 9, 5]
Range - 6

Remove 4 and add 10
Heap [5, 9, 10]
Range - 6

and so on....

Finally you will yield the result.
'''

#因为本身是sorted。 要让range变小，只能pop最小的边界，让最小边界变大

import heapq
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, arrs):
        h =[(arrs[i][0], i, 0) for i in range(len(arrs)) if arrs[i]]
        maxH = max(h)[0]
        heapq.heapify(h);  ret = []; minR = 10**10
        while True:
            val, i, j = heapq.heappop(h)
            if maxH-val<minR:     #keep track of the minimum window
                minR = maxH-val
                ret = (val, maxH)
            if j<len(arrs[i])-1:
                heapq.heappush(h, (arrs[i][j+1], i, j+1))
                maxH=max(maxH, arrs[i][j+1])
            else:  break
        return ret   #复杂度 O(nkLogk) 是最优解
#也可以合并后，

s= Solution()
print s.mergeKLists([[4, 10, 15, 24, 26] , [0, 9, 12, 20] ,  [5, 18, 22,  30]  ])
print s.mergeKLists([[1, 1001 ,2000], [20, 1001, 5000], [55, 1003, 222222]])

#另一个办法是用minimum window

'''
#minimum sliding window  。  merge K sorted arrays     用heap     nlog(k).
#暴力是用 nlogn
#第一步用merge k sorted arrays来做
#压成一个array  (1000, 0),  (1002, 2)
#sliding wind
#Minimum Window Substring
#只要合法。 不断更新。      index是sorted的数。  最小的窗口就是我们求的
#比leetcode稍微容易
class Solution:
    def find(arr, nRow):
        d={}; i =0;   ret = arr[-1][0]-arr[0][0]+10; x = (None, None)
        for t in arr:
            rNum=t[-1]; end=t[0]
            if rNum not in d: d[rNum]=0
            d[rNum]+=1
            if len(d)==nRow: #缩减窗口
                while d[arr[i][-1]]>1:
                    d[arr[i][-1]]-=1
                    i+=1
                start = arr[i][0]
                if end - start+1<ret:
                    x =(start, end)
                    ret = end - start+1
        return x         #O(n)
#稍微改变的版本
'''