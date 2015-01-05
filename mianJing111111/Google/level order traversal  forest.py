# encoding=utf-8
'''
we can define the concept of a "forest" as a
      set of 0 or more disjoint trees.

      1. Example:
                        B       C       E
                                |     /   \
                                D     F   G
                                          |
                                          H

      2. Observe: we can convert a forest to a tree by adding a single node
         to serve as the root of a tree in which each of the original trees
         is a subtree:

        ex:                     A
                            /   |   \
                        B       C       E
                                |     /   \
                                D     F   G
                                          |
                                          H

      3. Conversely, deleting the root from a tree leaves behind a forest
         consisting of its subtrees.  (Obviously, this is how we got our
         forest from our original tree.)
'''
#基本上一样。就改了一句
class Solution:
    def levelOrder(self, roots):
        if not roots: return []
        pre, ret =roots, []   # 除了pre, cur之外，还用了第三个vals
        while pre:
            cur, vals = [], []     #必须用array。 因为是有序的。 并且不会有重复
            for n in pre:
                vals.append(n.val)
                if n.left:  cur.append(n.left)
                if n.right:  cur.append(n.right)
            ret.append(vals)
            pre = cur
        return ret