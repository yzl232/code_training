# encoding=utf-8
'''
You need to find the inorder successor and predecessor of a given key. In case the given key is not found in BST, then return the two values within which this key will lie.

tree的题目递归都比较巧妙。 做过会很简单很快。 没做过会很难。 可以多刷
'''

class Solution:
    def findPreSuc(self, root, val):
        self.suc =self.prev =  None
        self.val = val
        self.dfs(root)
        return self.suc, self.prev

    def dfs(self, root):
        if not root: return
        if root.val == self.val:
            if root.left:
                tmp = root.left
                while tmp.right:  tmp = tmp.right
                self.prev = tmp
            if root.right:
                tmp = root.right
                while tmp.left:  tmp = tmp.left
                self.suc = tmp
        elif root.val>self.val:
            self.suc = root
            self.dfs(root.left)
        else:
            self.prev = root
            self.dfs(root.right)