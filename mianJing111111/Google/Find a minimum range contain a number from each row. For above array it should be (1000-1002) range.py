# encoding=utf-8
'''
G家考过

    Question is verbose, uses search engine, string matching
      etc., but at the end boils down to this: There is two dimensional array where each sub array (row) is sorted, i.e. [[1 1000 2000] [20 1001 5000] [55 1002 2222]] Find a minimum range contain a number from each row. For above array it should be (1000-1002) range.


'''

#因为本身是sorted。 所以我们放心pop最小的，因为拿上来的会变大

import heapq
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, arrs):
        h =[(arrs[i][0], i, 0) for i in range(len(arrs)) if arrs[i]]
        maxH = max(h)[0]
        heapq.heapify(h);  ret = []; minRange = 10**10
        while True:
            val, i, j = heapq.heappop(h)
            if maxH-val<minRange:     #keep track of the minimum window
                minRange = maxH-val
                ret = (val, maxH)
            if j<len(arrs[i])-1:
                heapq.heappush(h, (arrs[i][j+1], i, j+1))
                maxH=max(maxH, arrs[i][j+1])
            else:  #补满heap
                heapq.heappush(h, (val, i, j))                     #就加了这一句而已。
                break
        return ret   #复杂度 O(nkLogk) 是最优解
#也可以合并后，

s= Solution()
print s.mergeKLists([[4, 10, 15, 24, 26] , [0, 9, 12, 20] ,  [5, 18, 22, 30]  ])
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




#两种做法。 heap或者minimum window

'''
We have words and there positions in a paragraph in sorted order. Write an algorithm to find the least distance for a given 3 words.
eg. for 3 words
job: 5, 9 , 17
in: 4, 13, 18
google: 8, 19, 21
...
...
Answer: 17, 18, 19
Can you extend it to "n" words?

Context: In Google search results, the search terms are highlighted in the short paragraph that shows up. We need to find the shortest sentence that has all the words if we have word positions as mentioned above.
'''
#因为本身是sorted。 所以我们放心pop最小的，因为拿上来的会变大

import heapq
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, arrs):
        h =[(arrs[i][0], i, 0) for i in range(len(arrs)) if arrs[i]]
        maxH = max(h)[0]
        heapq.heapify(h);  ret = []; minRange = 10**10
        while True:
            val, i, j = heapq.heappop(h)
            if maxH-val<minRange:     #keep track of the minimum window
                minRange = maxH-val
                ret = (val, maxH)
            if j<len(arrs[i])-1:
                heapq.heappush(h, (arrs[i][j+1], i, j+1))
                maxH=max(maxH, arrs[i][j+1])
            else:  #补满heap
                heapq.heappush(h, (val, i, j))                     #就加了这一句而已。
                break
        return ret   #复杂度 O(nkLogk) 是最优解
#也可以合并后，