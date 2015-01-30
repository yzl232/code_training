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
    def levelOrder(self, roots):   # pre = cur这行 容易忘。 先写好这行。
        if not roots: return []
        pre, ret = [roots], [[roots.val]]   # 除了pre, cur之外
        while pre:
            cur = []     #必须用array。 因为是有序的。 并且不会有重复
            for n in pre:
                if n.left:  cur.append(n.left)
                if n.right:  cur.append(n.right)
            if cur: ret.append([x.val for x in cur])
            pre = cur
        return ret
