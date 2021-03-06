# encoding=utf-8


'''
就是一个常规的dfs。
无向的要难写一些。
#geeks上面喜欢用visited[]数组标记， 传入。  我就是直接用candidates， remove掉，再传入

我写的题目是找到所有的环。


无向的图可以换成有向的图。 基本上就是每个edge X 2.   这样子就一样了。 每个线段看成2个方向。


假如题目给的时   node,  neighbours. 只要我手动把它们转换成二元组就好。

'''

# 看看就好。第一部分是我自创的题目。。。
class Solution:
    def findCycle(self, graph):
        graph.sort()
        self.results =set([])
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
        for edge in candidates:
            if tmpPath[-1] in edge:  #这里与有向的区别。 线段2个中的任意一个端点与-1相同。
                tmpCan= candidates[:]
                tmpCan.remove(edge)
                if tmpPath[-1]==edge[0]: next = edge[1]
                else: next=edge[0]
                self.dfs(tmpPath+[next], tmpCan)

s = Solution()
print s.findCycle( [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4], [2, 6], [4, 6], [8, 7], [8, 9], [9, 7]])


#每个数是一个vertex.每个数组是一个edge。 用一堆edge就可以表示一个directed graphs了。


'''
neigbours

#find all cycles就用edge的方法做
其他都用二元做。


DFS的做法。  无向
'''

# 可以把visited变成self.visited。 然后visieted.add,  visited.remove()
#空间上更节省。

class Solution3:
    def paths(self, nodes):
        for n in nodes:
            if self.dfs([n], n, set([n])):  return True
        return False

    def dfs(self, cur, node, visited):  #visited传进去。 这是一个特别的地方。
        if len(cur)>2: cur=cur[-2:] #我只需要ppre
        for n in node.neighbors:
                if n==cur[-2]: continue  #因为长度必须大于2.  这是与有向图的唯一区别
                if n in visited:  return True
                t = visited.copy(); t.add(n)
                if self.dfs(cur+[n], n,t): return True
        return False