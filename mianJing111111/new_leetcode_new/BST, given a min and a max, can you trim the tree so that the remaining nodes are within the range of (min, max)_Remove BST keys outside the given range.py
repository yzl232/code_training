# encoding=utf-8
'''
BST, given a min and a max, can you trim the tree so that the remaining nodes are within the range of (min, max)
'''

class Solution:
    def solve(self, root):
        self.visited = set([])
        self.dfs(root)

    def dfs(self, root, minV, maxV):
        if not root: return
        if root in self.visited: return
        self.visited.add(root)
        if minV<=root.val<=maxV:
            root.left = self.dfs(root.left, minV, maxV)
            root.right = self.dfs(root.right, minV, maxV)
            return root
        elif root.val>maxV:
            l = root.left
            del root
            return l
        else:
            r = root.right
            del root
            return r


'''
#
#和geeks不一样。但是是正确的解法。
class Solution:
    def solve(self, root):
        self.visited = set([])
        self.dfs(root)

    def dfs(self, root, minV, maxV):
        if not root: return
        if root in self.visited: return
        self.visited.add(root)
        if minV<=root.val<=maxV:
            root.left = self.dfs(root.left, minV, maxV)
            root.right = self.dfs(root.right, minV, maxV)
            return root
        elif root.val>maxV: return self.dfs(root.left, minV, maxV)  #root右边以及root都被消除掉了
        else: return self.dfs(root.right, minV, maxV)  #root左边以及root都被消除掉了
'''