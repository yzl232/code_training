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

http://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/

和leetcode  那个single list 最优解是类似的

'''

class Solution:
    # @param root, a tree node  #注意这道题目不是binary search tree  。
    # @return nothing, do it in place  #他的顺序是   in order  left, root, right
    def flatten(self, root):  #我们反过来，就是right, root, left
        self.head = None
        self.dfs(root)

    def dfs(self, root):
        if not root: return
        self.dfs(root.right)
        if self.head:  self.head.left = root  #在这里，还可以设置tail节点。 如果有必要
        root.right = self.head  #右边连上
        self.head = root    #更新head
        self.dfs(root.left)

