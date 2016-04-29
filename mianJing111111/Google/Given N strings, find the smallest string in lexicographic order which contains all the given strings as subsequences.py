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
        h = [(x[0], i, 0) for i,x in enumerate(arrs) if x]
        heapq.heapify(h); ret= ""
        while h:
            ch, i, j = heapq.heappop(h)
            ret+=ch;  j+=1
            if j<len(arrs[i]): heapq.heappush(h, (arrs[i][j], i, j))
        return self.removeDup(ret)

    def removeDup(self, s):
        return "" if not s else s[0]+"".join(s[i] for i in range(1, len(s)) if s[i]!=s[i-1])


s = Solution()
print s.mergeKLists(['abc', 'aef', 'az', 'bep', 'za'])
#好处是代码特别短。    #复杂度 O(nkLogk) 是最优解