# encoding=utf-8
'''
Given N strings, find the smallest string in lexicographic order which contains all the given strings as subsequences
'''
#n-way merge .  用heap来做。 就是注意最后消去连续的重复的部分。比如baaab  变成bab


# python里边。string基本和array一样
#因为是subsequence。每个要保留其相对顺序。
import  heapq
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, arrs):
        h =[(arrs[i][0], i, 0) for i in range(len(arrs)) if arrs[i]]
        heapq.heapify(h);  ret = ''
        while h:
            val, i, j = heapq.heappop(h)
            ret+=val
            if j+1<len(arrs[i]):  heapq.heappush(h, (arrs[i][j+1], i, j+1))
        ret = self.removeDup(ret)
        return ret

    def removeDup(self, s):
        if not s: raise ValueError('Empty result')
        ret = s[0]
        for i in range(1, len(s)):
            if s[i]==s[i-1]: continue
            ret+=s[i]
        return ret


s = Solution()
print s.mergeKLists(['abc', 'aef', 'az', 'bep', 'za'])
#好处是代码特别短。    #复杂度 O(nkLogk) 是最优解