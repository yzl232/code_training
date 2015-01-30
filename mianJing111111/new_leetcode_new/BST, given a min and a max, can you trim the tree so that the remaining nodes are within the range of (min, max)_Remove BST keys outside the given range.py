# encoding=utf-8
'''
BST, given a min and a max, can you trim the tree so that the remaining nodes are within the range of (min, max)
'''



class Solution:
    def trim(self, root, minV, maxV):  # post order
        if not root: return
        root.left = self.trim(root.left, minV, maxV)
        root.right = self.trim(root.right, minV, maxV)
        if minV<=root.val<=maxV: return root
        elif root.val>maxV: return root.left
        else: return root.right

# 基本上什么mirror tree,  delete tree，  trim 这种改变树的结构的题目， 做法都是用post order 的


#之前莫名有了误解。  left, right都是往下找。 不会有回溯的。

#下面这个是垃圾。
'''
#
#和geeks不一样。但是是正确的解法。
class Solution:
    def trim(self, root, minV, maxV):
        if not root: return
        if minV<=root.val<=maxV:
            root.left = self.trim(root.left, minV, maxV)
            root.right = self.trim(root.right, minV, maxV)
            return root
        elif root.val>maxV:   return self.trim(root.left, minV, maxV)  #root右边以及root都被消除掉了
        else: return self.trim(root.right, minV, maxV)  #root左边以及root都被消除掉了
'''