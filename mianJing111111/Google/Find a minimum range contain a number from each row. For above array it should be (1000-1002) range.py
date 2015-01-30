# encoding=utf-8
'''
G家考过

    Question is verbose, uses search engine, string matching
      etc., but at the end boils down to this: There is two dimensional array where each sub array (row) is sorted, i.e. [[1 1000 2000] [20 1001 5000] [55 1002 2222]] Find a minimum range contain a number from each row. For above array it should be (1000-1002) range.


'''

#可以这样想象  。 range:  minV~maxV。  每次minhEap移除minV。  来尝试得到更小的范围
#每次push之前得到最大。 pop的是最小。  最大减去最小就是range


# F家也考过
#因为本身是sorted。 所以我们放心pop最小的，因为拿上来的会变大


#加入本身不是sorted。 那么sort一下。
import heapq
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, arrs):  #可以raise error如果某个为空。
        for x in arrs:
            if not x: raise ValueError
        h =[(arrs[i][0], i, 0) for i in range(len(arrs)) ]
        maxH = max(h)[0]; ret=(0, 0, 10**10)
        heapq.heapify(h);
        while h:
            val, i, j = heapq.heappop(h)
            if maxH-val<ret[-1]:        ret = (val, maxH, maxH-val)              #keep track of the minimum window
            j+=1
            if j<len(arrs[i]):
                heapq.heappush(h, (arrs[i][j], i, j))
                maxH=max(maxH, arrs[i][j])   #  push的同时更新maxH
            else:         break  #有某行为空了。 停止break。   这时候minV固定了。。。
        return ret   #复杂度 O(nkLogk) 是最优解
#也可以合并后，
s= Solution()
print s.mergeKLists([[4, 10, 15, 24, 26] , [0, 9, 12, 20] ,  [5, 18, 22, 30]  ])
print s.mergeKLists([[1, 1001 ,2000], [20, 1001, 5000], [55, 1003, 222222]])
print s.mergeKLists([[1000], [1, 200], [4, 800]])
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




#两种做法。 heap或者minimum window


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