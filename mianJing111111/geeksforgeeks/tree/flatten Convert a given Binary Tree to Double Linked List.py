# encoding=utf-8
'''
Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be head node of the DLL.


http://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/

转化成inorder的。


1. If left subtree exists, process the left subtree
…..1.a) Recursively convert the left subtree to DLL.
…..1.b) Then find inorder predecessor of root in left subtree (inorder predecessor is rightmost node in left subtree).
…..1.c) Make inorder predecessor as previous of root and root as next of inorder predecessor.
2. If right subtree exists, process the right subtree (Below 3 steps are similar to left subtree).
…..2.a) Recursively convert the right subtree to DLL.
…..2.b) Then find inorder successor of root in right subtree (inorder successor is leftmost node in right subtree).
…..2.c) Make inorder successor as next of root and root as previous of inorder successor.
3. Find the leftmost node and return it (the leftmost node is always head of converted DLL).



we are not allowed to create a new list,
we have to convert the given tree itself into doubly linked list..

不准用extra的内容。 必须用double linked list.


简单的想法是 in-order traversal  然后插入。O(n) space

难就难在 in-place


'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bintree2List(self, root):
        if not root: return root
        root = self.dfs(root)
        while not root.left:
            root = root.left
        return root

    def dfs(self, root):
        if not root: return root
        if root.left:
            left = self.dfs(root.left)     #Convert the left subtree and link to root
            while left.right: left = left.right  ##找到左边最靠右的连上
            left.right = root     #Make root as next of the predecessor
            root.left = left    # Make predecssor as previous of root
        if root.right:
            right = self.dfs(root.right)  ##找到右边最靠左的连上
            while right.left:  right = right.left
            right.left = root
            root.right = right
        return root  #recursion 都是返回自己。