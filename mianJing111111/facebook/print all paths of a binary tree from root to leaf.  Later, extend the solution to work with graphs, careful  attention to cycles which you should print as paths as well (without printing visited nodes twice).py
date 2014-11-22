# encoding=utf-8
'''

Print all paths of a binary tree from root to leaf.

Later, extend the solution to work with graphs, careful attention to cycles which you should print as paths as well (without printing visited nodes twice).

#和graph里面的一样的。 找环类似。  有向图。



就是普通的DFS. 加上一个hashmap标记。

'''
class Solution:
    def printPaths(self, node):
        if not node: return []
        self.d = {}
        self.results = []
        self.dfs(node,  [node.label])  #提前
        return self.results

    def dfs(self, root, tmpPath):
        if root in self.d:
            self.results.append(tmpPath)
            return
        self.d[root] = True
        if root.left and not root.right:
            self.results.append(tmpPath)
            return
        if root.left:  self.dfs(root.left,  tmpPath+[root.left.label] )
        if root.right:  self.dfs(root.right,  tmpPath+[root.right.label] )