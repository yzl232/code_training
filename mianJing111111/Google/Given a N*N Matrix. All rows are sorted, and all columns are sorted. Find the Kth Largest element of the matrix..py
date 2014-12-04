# encoding=utf-8
'''


    Question is verbose, uses search engine, string matching
      etc., but at the end boils down to this: There is two dimensional array where each sub array (row) is sorted, i.e. [[1 1000 2000] [20 10001 5000] [55 10002 222222]] Find a minimum range contain a number from each row. For above array it should be (1000-1002) range.


'''

'''

You can do this in 2n iterations. The idea is to find a range (starting from the left side), which is feasible (i.e. contains at least one value from each row). The range is determined by the indices [start_idx, end_idx]. In each iteration, if we can decrease the interval by moving start_idx forward, then we do that (which gives us a potentially smaller range), otherwise we increase the range by incrementing end_idx by one. This will have a running time of 2n (where n is the total number of values in all rows) since the start and end indices are only ever moved forwards.
'''

'''
Merge the arrays and uniquify the values, and then run a sliding window over the sorted values. To find the minimal sliding window, maintain two pointers, incrementing the right one if the range is too small, and incrementing the left one once the range becomes too large. This is a standard technique for finding minimal/maximal ranges in linear time whenever the target is monotonic.

'''

#minimum sliding window  。  merge K sorted arrays     用merge sort.      nlog(k).
#暴力是用 nlogn
#第一步用merge k sorted arrays来做
#压成一个array  (1000, 0),  (1002, 2)
#sliding wind
#Minimum Window Substring
#只要合法。 不断更新。      index是sorted的数。  最小的窗口就是我们求的
#比leetcode稍微容易
class Solution:
    def find(arr, nRow):
        d={}; i =0;   minL = arr[-1][0]-arr[0][0]+10; ret = (None, None)
        for r in arr:
            rN=r[-1]; end=r[0]
            if rN not in d: d[rN]=0
            d[rN]+=1
            if len(d)==nRow: #缩减窗口
                while d[arr[i][-1]]>1:
                    d[arr[i][-1]]-=1
                    i+=1
                st = arr[i][0]
                if end - st+1<minL:
                    ret =(st, end)
                    minL = end - st+1
        return ret         #O(n)
#minimum window substring    稍微改变的版本