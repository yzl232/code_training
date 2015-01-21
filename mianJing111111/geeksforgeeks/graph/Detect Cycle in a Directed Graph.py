# encoding=utf-8

# encoding=utf-8


'''
我的习惯是把每个图用一堆edge表示。 每个edge就是一个二元数组。


就是一个常规的dfs。
与无向的区别只在于next的选择和一定要第一个数等于tmpPath[-1].
然后2个数就可以是一个cycle。  无向至少3个。

无向的其实更难一点.  有向的，其实我做过。。
'''

# 看看就好。第一部分是我自创的题目。。。
class Solution:
    def findCycle(self, graph):
        graph.sort()
        self.ret = []
        self.d = {}
        for edge in graph:
            candidates = graph[:] #注意冒号。 更新candidates
            candidates.remove(edge) #注意remove不返回值的。
            self.dfs(edge[:], candidates)
        return self.ret

#[1, 2],  [2, 8],  [1,  8]
    def dfs(self, cur, candidates):
        if len(cur)>2 and cur[-1]==cur[0]:    #
            a = cur[:-1]; ta = tuple(sorted(a))
            if ta not in self.d:
                self.d[ta] = 1
                self.ret.append(a)
            return
        for edge in candidates:
            if cur[-1] == edge[0]:
                tmpCan= candidates[:]
                tmpCan.remove(edge)
                self.dfs(cur+[edge[-1]], tmpCan)

s = Solution()
print s.findCycle( [[1, 2], [1, 3], [4, 1], [3, 2], [3, 4], [2, 6], [4, 6], [8, 7], [9, 8], [7, 9]])


#每个数是一个vertex.每个数组是一个edge。 用一堆edge就可以表示一个directed graphs了。

'''
neigbours

#find all cycles就用edge的方法做
其他都用二元做。


DFS的做法。  有向
'''

# 可以把visited变成self.visited。 然后visieted.add,  visited.remove()
#空间上更节省。

class Solution3:
    def paths(self, nodes):
        for n in nodes:
            if self.dfs(n, set([n])):  return True
        return False

    def dfs(self, node, visited):  #visited传进去。 这是一个特别的地方。
        for n in node.neighbors:
                if n in visited:   return True
                t=visited.copy(); t.add(n)
                if self.dfs(n, t): return True
        return False