# encoding=utf-8
'''
BST, given a min and a max, can you trim the tree so that the remaining nodes are within the range of (min, max)
'''
class Solution:
    def trim(self, root, minV, maxV):
        if not root: return
        if minV<=root.val<=maxV:
            root.left = self.trim(root.left, minV, maxV)
            root.right = self.trim(root.right, minV, maxV)
            return root
        elif root.val>maxV:
            return self.trim(root.left)
        else: return self.trim(root.right)