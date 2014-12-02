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
class Solution:
    def mirror(self, root):
        if not root:
            return
        self.mirror(root.left)
        self.mirror(root.right) #先recursion  子树以后，再弄父节点。
        root.left, root.right =  root.right, root.left