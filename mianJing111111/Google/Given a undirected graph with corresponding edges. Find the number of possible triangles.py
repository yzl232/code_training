# encoding=utf-8
'''
Given a undirected graph with corresponding edges. Find the number of possible triangles

Example:
0 1
2 1
0 2
4 1

Answer:
1
'''
#有点像无向图找环。  目标是找三个点的环。

#http://www.vertica.com/2011/09/21/counting-triangles/
#解释的比较清楚

class Solution:
    def findCycle(self, graph):
        graph.sort()
        self.results = []
        self.d = {}    #主要是查重复的环。
        for edge in graph:
            candidates = graph[:] #注意冒号。 更新candidates
            candidates.remove(edge) #注意remove不返回值的。
            self.dfs(list(edge), candidates)
        return self.results

#[1, 2],  [2, 8],  [1,  8]
    def dfs(self, tmpPath, candidates):
        if len(tmpPath)>3 and tmpPath[-1]==tmpPath[0]:  #有向图长度为2也可以是环。 无向要3.
            a = tmpPath[:-1]; ta = tuple(sorted(a))
            if ta not in self.d:  #
                self.d[ta] = 1
                self.results.append(a)
            return
        if len(tmpPath)>=4: return
        for edge in candidates:
            if tmpPath[-1] in edge:  #这里与有向的区别。 线段2个中的任意一个端点与-1相同。
                tmpCan= candidates[:]
                tmpCan.remove(edge)
                if tmpPath[-1]==edge[0]: next = edge[1]
                else: next=edge[0]
                self.dfs(tmpPath+[next], tmpCan)
s = Solution()
print s.findCycle( [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4], [2, 6], [4, 6], [8, 7], [8, 9], [9, 7]])

#The total number of triangles will be the number of triangles we counted divided by 6 (we count each triangle 6 times).

#假如不用hashmap  sort 去重，就是cnt/6

# O(n^3)   因为三角形。 每个点都是暴力搜索。  n*n*n