# encoding=utf-8
'''


Maximum width of a binary tree

Given a binary tree, write a function to get the maximum width of the given tree. Width of a tree is maximum of widths of all levels.

Let us consider the below example tree.

         1
        /  \
       2    3
     /  \     \
    4    5     8
              /  \
             6    7

For the above tree,
width of level 1 is 1,
width of level 2 is 2,
width of level 3 is 3
width of level 4 is 2.

So the maximum width of the tree is 3.

和我想象的不一样。 我以为只是普通的vertical。 不是的。
还是普通的level order
'''
class Solution:
    def levelOrder(self, root):
        if not root: return 0
        prev, res = [root], 1
        while prev:
            cur = []
            for node in prev:
                if node.left:  cur.append(node.left)
                if node.right:  cur.append(node.right)
            prev = cur
            res = max(res, len(cur))
        return res