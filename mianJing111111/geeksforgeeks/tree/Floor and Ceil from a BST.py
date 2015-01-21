# encoding=utf-8
'''

Floor and Ceil from a BST

There are numerous applications we need to find floor (ceil) value of a key in a binary search tree or sorted array. For example, consider designing memory management system in which free nodes are arranged in BST. Find best fit for the input request.

Ceil Value Node: Node with smallest data larger than or equal to key value.

Imagine we are moving down the tree, and assume we are root node. The comparison yields three possibilities,

A) Root data is equal to key. We are done, root data is ceil value.

B) Root data < key value, certainly the ceil value can’t be in left subtree. Proceed to search on right subtree as reduced problem instance.

C) Root data > key value, the ceil value may be in left subtree. We may find a node with is larger data than key value in left subtree, if not the root itself will be ceil node.


天花板， 地板
'''
#可以用暴力法。O(n).  就是in order 。 if not self.ceil:  找第一个大于等于的值。
#最佳的是下面的，O(logN)
#理一下逻辑.  也利用了return的值
class Solution:
    def ceil(self, root, val):
        ret = None
        while root:
            if root.val==val: return val
            elif root.val<val:root=root.right
            else:
                ret = root.val
                root = root.left
        return ret
    
    def floor(self, root, val):
        ret = None
        while root:
            if root.val==val: return val
            elif root.val>val:root=root.left
            else:
                ret = root.val
                root = root.right
        return ret
    
    '''
    def ceil(self, root, val):
        if not root: return
        if root.val == val: return val
        elif root.val < val:   return self.ceil(root.right, val)
        else:
            c=self.ceil(root.left, val)
            if c: return c
            return root.val
    # floor只是左右变换一下而已
    def floor(self, root, val):
        if not root: return
        if root.val == val: return val
        elif root.val>val:
            return self.floor(root.left, val)
        else:
            f = self.floor(root.right, val)
            if f: return f
            return root.val
    '''