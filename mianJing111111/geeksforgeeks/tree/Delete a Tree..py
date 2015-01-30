# encoding=utf-8
'''
To delete a tree we must traverse all the nodes of the tree and delete them one by one. So which traversal we should use – Inorder or Preorder or Postorder. Answer is simple – Postorder, because before deleting the parent node we should delete its children nodes first

We can delete tree with other traversals also with extra space complexity but why should we go for other traversals if we have Postorder available which does the work without storing anything in same time complexity.

For the following tree nodes are deleted in order – 4, 5, 2, 3, 1


后序
'''

# # 基本上什么mirror tree,  delete tree，  trim 这种改变树的结构的题目， 做法都是用post order 的

class Solution:
    def deleteTree(self, root):
        if not root: return
        self.deleteTree(root.left)
        self.deleteTree(root.right)
        del root