# encoding=utf-8
'''

Construct Complete Binary Tree from its Linked List Representation

Given Linked List Representation of Complete Binary Tree, construct the Binary tree. A complete binary tree can be represented in an array in the following approach.

If root node is stored at index i, its left, and right children are stored at indices 2*i+1, 2*i+2 respectively.
Suppose tree is represented by a linked list in same way, how do we convert this into normal linked representation of binary tree where every node has data, left and right pointers? In the linked list representation, we cannot directly access the children of the current node unless we traverse the list.



geeks这道题目是level order的变体.   用BFS
不需要vals。   区别就在于， 多了建立树，以及连接left, right的过程
另外while的标准变成了head
'''

#和这道题目是兄弟   check whether a given binary tree is complete or not


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
        while prev:
            if not head: break
            cur = []
            for node in prev:
                if head:
                    x = TreeNode(head.val)
                    head = head.next
                    node.left = x
                    cur.append(x)
                if head:
                    x = TreeNode(head.val)
                    head = head.next
                    node.right = x
                    cur.append(x)
            prev = cur
        return root