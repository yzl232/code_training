# encoding=utf-8
# 俄罗斯方块，每一个图案都是由4个block组成，现在给定一个N表示N个block，把所有
# 有效的俄罗斯方块组合都输出出来
'''
我的想法。 找所有的四元tuple().  要求是相邻的a1, a2, a3, a4.  并且a1<a4.
这样子可以识别每一个四元tuple， 都是unique

每次找到所有tuple。
用一个notVisited的set表示没有经过的点。



if not  noVisted:
    self.ret.append(cur)
    return True
fours = self.bfs(i, j)
for x in fours:
    如果a1>a4: reverse
for x in fours:
    if self.dfs(cur+x,  ,  Novisited):


'''