# encoding=utf-8
'''
You need to find the inorder successor and predecessor of a given key. In case the given key is not found in BST, then return the two values within which this key will lie.

无所谓哪种traversal都可以做。
'''

#O(logN)实际上就可以做.
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


#inorder就可以做了.   不过是O(n)。 相当于暴力解法了。 用了2个指针
class Solution:
    def findSucPre(self, root, v):
        self.pre = None; self.suc=None
        self.dfs(root, v)
        return self.dfs(root)

    def dfs(self, root, v):
        if not root: return
        self.dfs(root.left, v)
        if root.val>v:
            if not self.suc: self.suc=root.val
            self.suc = min(self.suc, root.val)
        elif root.val<v:
            if not self.pre: self.pre=root.val
            self.pre = max(self.pre, root.val)
        self.dfs(root.right, v)