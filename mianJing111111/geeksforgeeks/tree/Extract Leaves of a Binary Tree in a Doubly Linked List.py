# encoding=utf-8
'''

Extract Leaves of a Binary Tree in a Doubly Linked List

Given a Binary Tree, extract all leaves of it in a Doubly Linked List (DLL). Note that the DLL need to be created in-place. Assume that the node structure of DLL and Binary Tree is same, only the meaning of left and right pointers are different. In DLL, left means previous pointer and right means next pointer.

Let the following be input binary tree
        1
     /     \
    2       3
   / \       \
  4   5       6
 / \         / \
7   8       9   10


Output:
Doubly Linked List
7<->8<->5<->9<->10

Modified Tree:
        1
     /     \
    2       3
   /         \
  4           6

We strongly recommend you to minimize the browser and try this yourself first.

We need to traverse all leaves and connect them by changing their left and right pointers. We also need to remove them from Binary Tree by changing left or right pointers in parent nodes. There can be many ways to solve this. In the following implementation, we add leaves at the beginning of current linked list and update head of the list using pointer to head pointer. Since we insert at the beginning, we need to process leaves in reverse order. For reverse order, we first traverse the right subtree then the left subtree. We use return values to update left or right pointers in parent nodes.


取出所有的叶子。
'''
class Solution:
    def extractLeafList(self, root, head):
        self.head = None
        self.dfs(root)
        return self.head

    def dfs(self, root):
        if not root: return
        if not root.left and not root.right:
            root.right = self.head
            if self.head:  self.head.left = root
            self.head = root
            return
        root.right = self.dfs(root.right)  #root作为parent的情况。   不好写。 背下吧.  解法简洁。不好写。
        root.left = self.dfs(root.left)
        return root

'''
G算法题
就是一棵树或者森林，让你依次摘掉并打印叶节点；然后循环上述步骤，直到把树消干净
'''
class Solution9:
    def removeLeaves(self, root, head):
        while root:
            root = self.dfs(root)
        return self.head

    def dfs(self, root):
        if not root: return
        if not root.left and not root.right:
            print root.val
            return
        root.right = self.dfs(root.right)  #root作为parent的情况。   不好写。 背下吧.  解法简洁。不好写。
        root.left = self.dfs(root.left)
        return root