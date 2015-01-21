class Solution6:
    def checkLevel(self, root):
        return self.dfs(root, 0)

    def dfs(self, root, lvl):
        if not root: return lvl
        if root.left and root.right: return min(self.dfs(root.left, lvl+1), self.dfs(root.right, lvl+1))
        return lvl+1