# encoding=utf-8
'''
You need to find the inorder successor and predecessor of a given key. In case the given key is not found in BST, then return the two values within which this key will lie.

无所谓哪种traversal都可以做。
'''

#O(logN)实际上就可以做.  找一个，可以logN。类似binary search
class Solution:
    def findPreSuc(self, root, val):
        self.suc =self.prev =  None
        self.x = val
        self.dfs(root)
        return self.suc, self.prev

    def dfs(self, root):
        if not root: return
        if root.val == self.x:
            if root.left:
                t = root.left
                while t.right:  t = t.right
                self.prev = t
            if root.right:
                t = root.right
                while t.left:  t = t.left
                self.suc = t
        elif root.val>self.x:
            self.suc = root #太大了。 用h压一压。   和binary search一个思路
            self.dfs(root.left)
        else:             #注意这个elif , else  ，  就是binary  search.
            self.prev = root
            self.dfs(root.right)
#基本上就是binary search
'''
def bs(arr, x):
    l=0; h=len(arr)-1
    while l<=h:
        m = (l+h)/2
        if m==x: return x
        elif m<x: l=m+1
        else: h=m-1
'''



#inorder就可以做了.   不过是O(n)。 相当于暴力解法了。 用了2个指针
class Solution4:
    def findSucPre(self, root, v):
        self.pre = None; self.suc=None
        self.dfs(root, v)
        return self.dfs(root)

    def dfs(self, root, v):
        if not root: return
        self.dfs(root.left, v)
        if root.val>v:
            if not self.suc: self.suc=root.val
            # self.suc = min(self.suc, root.val) 这一句可以略去。 因为是从最小到最大。
        elif root.val<v:
            if not self.pre: self.pre=root.val
            self.pre = max(self.pre, root.val)
        self.dfs(root.right, v)