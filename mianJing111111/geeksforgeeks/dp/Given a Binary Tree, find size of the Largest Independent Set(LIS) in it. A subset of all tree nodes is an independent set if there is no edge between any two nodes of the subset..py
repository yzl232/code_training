# encoding=utf-8
'''
Given a Binary Tree, find size of the Largest Independent Set(LIS) in it. A subset of all tree nodes is an independent set if there is no edge between any two nodes of the subset.
For example, consider the following binary tree. The largest independent set(LIS) is {10, 40, 60, 70, 80} and size of the LIS is 5.



Let LISS(X) indicates size of largest independent set of a tree with root X.

     LISS(X) = MAX { (1 + sum of LISS for all grandchildren of X),
                     (sum of LISS for all children of X) }

noRoot  = CurMax(root.left)+curMax(root.right)
WithRoot = noRoot(root.left)+noROot(root.right)+1
curMax = max(noRoot,  WithRoot)


'''
# excl 有2个。  incl有5个。

class Solution(object):
    def rob(self, root):
        def dfs(x):
            if not x: return (0, 0)
            l, r = dfs(x.left), dfs(x.right)
            return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + 1))
        return dfs(root)[1]

# https://leetcode.com/problems/house-robber-iii/

'''
noRoot(node) = curMax(node.left) + curMax(node.right)

curMax(node) = max( noRoot(node.left)+noRoot(node.right)+node.value, noRoot(node) ).
'''
#有点像这道题。 geeks: Given a Binary Tree, find size of the Largest Independent Set(LIS)
'''
#递归
class Solution:
    def liss(self, root):
        if not root: return 0
        excl = self.liss(root.left)+self.liss(root.right)
        incl = 1
        if root.left:     incl+=self.liss(root.left.left) + self.liss(root.left.right)
        if root.right:  incl+=self.liss(root.right.left) + self.liss(root.right.right)
        return max(excl, incl)

#dp.    {memoization}
# memoization思想在于return的时候先不return。 而是存到hashmap里边去。
class Solution1:
    d ={}
    def liss(self, root):
        if not root: return 0
        if root in self.d: return self.d[root]
        size_excl = self.liss(root.left)+self.liss(root.right)
        size_incl = 1
        if root.left:      size_incl+=self.liss(root.left.left) + self.liss(root.left.right)
        if root.right:    size_incl+=self.liss(root.right.left) + self.liss(root.right.right)
        self.d[root] =  max(size_excl, size_incl)
        return self.d[root]
'''