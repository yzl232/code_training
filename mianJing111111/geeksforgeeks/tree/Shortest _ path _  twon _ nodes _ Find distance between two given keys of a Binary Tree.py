# encoding=utf-8
'''
Find the distance between two keys in a binary tree, no parent pointers are given. Distance between two nodes is the minimum number of edges to be traversed to reach one node from other.


 Time complexity of the above solution is O(n) as the method does a single tree traversal.

 Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca)

'lca' is lowest common ancestor of n1 and n2
Dist(n1, n2) is the distance between n1 and n2.

geeks是正确的。 只是自己理解不够正确。

        1
    2      3
 4    5

要验证。只要跑简单的例子就好

'''

class SolutionRecursin:
    def findAncestor(self, root, p, q, lvl):
        if not root: return
        if root == p :
            self.d1 = lvl  #Dist(root, n1)   d1的意思。
            return root
        elif root ==q:
            self.d2 = lvl
            return root
        l = self.findAncestor(root.left, p, q, lvl+1)
        r = self.findAncestor(root.right, p, q, lvl+1)
        if l and r:
            self.distance = self.d1+self.d2-2*lvl
            return root  #2个都找到。在root.    分布在root左右两边
        if l: return l  #找到一个。在左边
        else: return r  #找到一个。在右边

    def findLevel(self, root, level): #找一个子节点到root得距离
        if not root: return -1
        if root == self.node: return level
        d = self.findLevel(root.left, level+1)
        if d==-1:
            d = self.findLevel(root.right,  level+1)
        return d

    def findDistance(self, root, n1, n2, level):
        self.d1 = self.d2 =self.distance = -1
        lca = self.findDistance(root, n1, n2, 0)
        if lca!=n1 and lca != n2: return self.distance
        if lca==n1:    #  If n1 is ancestor of n2, consider n1 as root and find level of n2 in subtree rooted with n1...     n2 没有更新。 是子节点。
            self.node = n2    #
            return  self.findLevel(n1, 0)
        if lca==n2:
            self.node = n1
            return self.findLevel(n2, 0)
'''
也就是三种情况  。
n1是N2的父节点。  这样子。找ancestor的时候，直接无视了N2
N2是n1的父节点。
普通情况。 这时候，某个递归里边。 已经update了 self.distance
'''