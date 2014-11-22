# encoding=utf-8
'''

Rearrange a string so that all same characters become d distance away

Given a string and a positive integer d. Some characters may be repeated in the given string. Rearrange characters of the given string such that the same characters become d distance away from each other. Note that there can be many possible rearrangements, the output should be one of the possible rearrangements. If no such arrangement is possible, that should also be reported.
Expected time complexity is O(n) where n is length of input string.

Examples:
Input:  "abb", d = 2
Output: "bab"

Input:  "aacbbc", d = 3
Output: "abcabc"

Input: "geeksforgeeks", d = 3
Output: egkegkesfesor

Input:  "aaa",  d = 2
Output: Cannot be rearranged



#贪心的算法。 找到频率最高的ch。 从左边排列好。
'''

import heapq
class Solution:
    def rearrange(self, s, distance):
        n = len(s)
        d = {}
        for ch in s:
            if ch not in d: d[ch]=0
            d[ch]+=1
        arr = [-1 for i in range(n)]
        a = []
        heapq.heapify(a)
        m = len(d)
        for ch in d:
            heapq.heappush(a, (0-d[ch], ch))  #我这里用负数。解决了max Heap.   min Heap 的问题
        for i in range(m):
            tmp = heapq.heappop(a)      #每次弹出频率最高的。
            freq = 0-tmp[0]; ch =tmp[1]
            start = None
            for k in range(n):
                if arr[k]==-1:     #找到填充的起点。
                    start = k
                    break
            for k in range(freq):
                if start+k*distance >=n:
                    print "Cannot be rearranged"
                    return
                arr[start+k*distance] = ch
        return ''.join(arr)





s = Solution()
print s.rearrange("geeksforgeeks", 3)