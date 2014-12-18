# encoding=utf-8
'''

Print all paths of a binary tree from root to leaf.

Later, extend the solution to work with graphs, careful attention to cycles which you should print as paths as well (without printing visited nodes twice).

#和graph里面的一样的。 找环类似。  有向图。
  


就是普通的DFS. 加上一个hashmap标记。
然后就是left ,right 变成 neigbors.


#假定有向图
'''
class Solution:
    def printPaths(self, node):
        if not node: return []
        self.d = {}
        self.rets = []
        self.dfs(node,  [])
        return self.ret

    def dfs(self, n, cur): #cur path
        if n in self.d:
            self.rets.append(cur+[n.label])
            return
        self.d[n] = True
        for x in n.neighbors:
            #    if cur and cur[-1]==x: continue  无向图要加上这句
            self.dfs(x, cur+[n.label])