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
# 可以把visited变成self.visited。 然后visieted.add,  visited.remove()
#空间上更节省一点。


class Solution:
    def solve(self, arr):   #这道题目必须用到所有的string
        if not arr: raise ValueError
        return  self.dfs( arr[:1], arr[1:])

    def dfs(self, cur, rest):
        if not rest:   return cur[0][0] == cur[-1][-1]
        for x in rest:
            if x[0]==cur[-1][-1]:
                t = rest[:]; t.remove(x)
                if self.dfs(cur+[x] ,t): return True
        return False



#pass
s = Solution()
print s.solve(["for", "geek", "rig", "kaf"])