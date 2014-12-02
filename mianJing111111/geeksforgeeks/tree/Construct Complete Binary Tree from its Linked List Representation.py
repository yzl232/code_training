# encoding=utf-8
'''

Construct Complete Binary Tree from its Linked List Representation

Given Linked List Representation of Complete Binary Tree, construct the Binary tree. A complete binary tree can be represented in an array in the following approach.

If root node is stored at index i, its left, and right children are stored at indices 2*i+1, 2*i+2 respectively.
Suppose tree is represented by a linked list in same way, how do we convert this into normal linked representation of binary tree where every node has data, left and right pointers? In the linked list representation, we cannot directly access the children of the current node unless we traverse the list.



geeks这道题目是level order的变体.   用BFS
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bfs(self, head):
        if not head: return
        root = TreeNode(head.val)
        head = head.next
        prev= [root]
        while head:
            cur, vals = [], []
            for node in prev:
                if head:
                    l = TreeNode(head.val)
                    head = head.next
                    node.left = l
                    cur.append(l)
                if head:
                    r = TreeNode(head.val)
                    head = head.next
                    node.right = l
                    cur.append(l)
            prev = cur
        return root