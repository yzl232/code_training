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
因为不用push。比较特别。所以是O(n)
'''

import heapq
class Solution:
    def rearrange(self, s, dist):
        n = len(s);  d = {}; start=0
        for ch in s:
            if ch not in d: d[ch]=0
            d[ch]+=1
        arr = [None] * n
        h = [(0-d[ch], ch) for ch in d]
        heapq.heapify(h)     #我这里用负数。解决了max Heap.   min Heap 的问题
        while h:
            p = heapq.heappop(h)      #每次弹出频率最高的。
            freq = 0-p[0]; ch =p[1]
            while arr[start]: start+=1    #找到填充的起点。
            for k in range(freq):  
                if start+k*dist >=n:  raise ValueError("can not be arranged")
                arr[start+k*dist] = ch
        return ''.join(arr)





s = Solution()
print s.rearrange("geeksforgeeks", 3)


'''
Time complexity of above implementation is O(n + mLog(MAX)). Here n is the length of str, m is count of distinct characters in str[] and MAX is maximum possible different characters.
'''