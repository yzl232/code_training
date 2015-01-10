# encoding=utf-8
#How to find the closest element to a given key value in a binary search tree?


#可以暴力用inorder traversL O(n)
#  找suc, pre可以做到O(logN)
def bs(arr, x):
    l=0; h=len(arr)-1
    while l<=h:
        m = (l+h)/2
        if m==x: return x
        elif m<x: l=m+1
        else: h=m-1

#类似有  if root.val <x: self.pre = root.val
class Solution:
    def findPreSuc(self, root, x):
        self.suc =self.prev =  None
        self.x = x; self.ret = None
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root: return
        if abs(root.val-self.x)<abs(self.ret-self.x): self.ret = root.val
        if root.val == self.x:      return
        elif root.val>self.x:     self.dfs(root.left)
        else:   self.dfs(root.right)