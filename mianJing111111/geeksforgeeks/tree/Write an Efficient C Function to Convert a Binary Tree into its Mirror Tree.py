# encoding=utf-8
'''
Write an Efficient C Function to Convert a Binary Tree into its Mirror Tree
   1
 /  \
3    2
        \
           4

          1
       /    \
     2        3
   /
4





'''
# # 基本上什么mirror tree,  delete tree，  trim 这种改变树的结构的题目， 做法都是用post order 的


class Solution:  #略类似delete
    def mirror(self, root):
        if not root: return
        self.mirror(root.left)
        self.mirror(root.right)
        root.left, root.right = root.right, root.left