# encoding=utf-8
'''
Given multiple stream of input numbers each of which may not fit in memory (we can assume each source to be individually sorted) give an API design to merge and store a fully sorted array. Design must be object oriented which can handle any number of input source types. Obviously output also cannot fit in memory
'''

# n-way merge
#用heap
#向N个stream读数的时候。 先每个stream读N个。 然后每次pop一个, 并读对应地stream一个。
import heapq

#heap和merge 复杂度一样。 但是heap代码只有8行。 merge代码要三倍
#三元tuple。存了本身array的位置，以及目前array的pointer。

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, arrs):
        h =[(arrs[i][0], i, 0) for i in range(len(arrs)) if arrs[i]]
        heapq.heapify(h);  ret = []
        while h:
            val, i, j = heapq.heappop(h)
            ret.append(val);  j+=1
            if j<len(arrs[i]):  heapq.heappush(h, (arrs[i][j], i, j))
        return ret   #复杂度 O(nkLogk) 是最优解
#好处是代码特别短。7行
#好处是代码特别短。# 。