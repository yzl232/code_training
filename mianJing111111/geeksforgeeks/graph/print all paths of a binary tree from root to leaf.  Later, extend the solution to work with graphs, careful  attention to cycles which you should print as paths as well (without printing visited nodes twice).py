# encoding=utf-8
'''

Print all paths of a binary tree from root to leaf.

Later, extend the solution to work with graphs, careful attention to cycles which you should print as paths as well (without printing visited nodes twice).

#和graph里面的一样的。 找环类似。  有向图。
  


就是普通的DFS. 加上一个hashmap标记。
然后就是left ,right 变成 neigbors.


#假定有向图
'''
# F家





#复制了有向图， 稍微修改
class Solution3:
    def paths(self, root):
        self.rets = []
        self.dfs(root, set([root]), [root])
        return self.rets

    def dfs(self, node, visited, cur):  #visited传进去。 这是一个特别的地方。
        if node in visited or not node.neighbors:   #空， 或者visited过了
            self.rets.append(cur)
            return
        for n in node.neighbors:
            t= visited.copy(); t.add(n)
            self.dfs(n, t, cur+[n])


'''

# 从一个node出发。 也是自创的题目。
class Solution:
    def printPaths(self, root):
        if not root: return []
        self.d = {}; self.rets = []
        self.dfs(root,  [root])
        return self.ret

    def dfs(self, n, cur): #cur path
        if n in self.d or not n.neighbors:
            self.rets.append(cur+[n])
            return
        self.d[n] = True
        for x in n.neighbors:
            self.dfs(x, cur+[n])  #    if cur and cur[-1]==x: continue  无向图要加上这句

'''