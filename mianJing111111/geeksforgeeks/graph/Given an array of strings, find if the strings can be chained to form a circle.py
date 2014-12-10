# encoding=utf-8
'''

Given an array of strings, find if the strings can be chained to form a circle

Given an array of strings, find if the given strings can be chained to form a circle. A string X can be put before another string Y in circle if the last character of X is same as first character of Y.

Examples:

Input: arr[] = {"geek", "king"}
Output: Yes, the given strings can be chained.
Note that the last character of first string is same
as first character of second string and vice versa is
also true.

Input: arr[] = {"for", "geek", "rig", "kaf"}
Output: Yes, the given strings can be chained.
The strings can be chained as "for", "rig", "geek"
and "kaf"

Input: arr[] = {"aab", "bac", "aaa", "cda"}
Output: Yes, the given strings can be chained.
The strings can be chained as "aaa", "aab", "bac"
and "cda"

Input: arr[] = {"aaa", "bbb", "baa", "aab"};
Output: Yes, the given strings can be chained.
The strings can be chained as "aaa", "aab", "bbb"
and "baa"

Input: arr[] = {"aaa"};
Output: Yes

Input: arr[] = {"aaa", "bbb"};
Output: No




建立环。  用DFS.
(word[0], word[-1]) 可以建立一个有向的edge


就是有向图的circle修改版本
'''
class Solution:
    def findCycle(self, words):
        graph = []
        for word in words:  graph.append((word[0], word[-1]))
        print graph
        self.results = []
        self.d = {}    #主要是查重复的环。
        for edge in graph:
            candidates = graph[:] #注意冒号。 更新candidates
            candidates.remove(edge) #注意remove不返回值的。
            self.dfs(list(edge), candidates)
        return self.results

#[1, 2],  [2, 8],  [1,  8]
    def dfs(self, tmpPath, candidates):
        if tmpPath[-1]==tmpPath[0] and len(candidates)==0:    #只有一个不同，就是len(candidates)==0
            a = tmpPath[:-1]; ta = tuple(sorted(a))
            if ta not in self.d:
                self.d[ta] = 1
                self.results.append(a)
            return
        for edge in candidates:
            if tmpPath[-1] == edge[0]:
                tmpCan= candidates[:]
                tmpCan.remove(edge)
                self.dfs(tmpPath+[edge[-1]], tmpCan)
s = Solution()
print s.findCycle(["for", "geek", "rig", "kaf"])