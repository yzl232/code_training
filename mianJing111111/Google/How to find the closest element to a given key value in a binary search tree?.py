# encoding=utf-8
#How to find the closest element to a given key value in a binary search tree?


#可以暴力用inorder traversL O(n)
#  找suc, pre可以做到O(logN)
'''
def bs(arr, x):
    l=0; h=len(arr)-1
    while l<=h:
        m = (l+h)/2
        if m==x: return x
        elif m<x: l=m+1
        else: h=m-1
'''
#类似有  if root.val <x: self.pre = root.val
class Solution:
    def findPreSuc(self, root, x):
        self.x = x; self.ret = root
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root: return
        if abs(root.val-self.x)<abs(self.ret-self.x): self.ret = root.val
        if root.val == self.x:      return
        elif root.val>self.x:     self.dfs(root.left)
        else:   self.dfs(root.right)

# 另一种办法就是找pre, and successor



# G家题。 变体
# 寻找BST中距离某个值最近的第二个元素。
class Solution9:
    def successor(self, root, target):   # binary search 的思想.  binary search val
        ret = None
        while root:
            if root.val>target:
                ret = root.val
                root=root.left
            else:  root=root.right
        return ret

    def predessor(self, root, target):
        ret = None
        while root:
            if root.val>target:  root=root.left
            else:
                ret = root.val
                root=root.right
        return ret

    def solve(self, root, target):
        if not root or (not root.left and not root.right): raise  ValueError()
        suc = self.successor(root, target)
        pre = self.predessor(root, target)
        if not suc: return self.predessor(root, pre)
        if not pre: return self.successor(root, suc)
        return suc if abs(suc-target)<abs(pre-target) else pre