# encoding=utf-8
'''


Convert a BST to a Binary Tree such that sum of all greater keys is added to every key

Given a Binary Search Tree (BST), convert it to a Binary Tree such that every key of the original BST is changed to key plus sum of all greater keys in BST.

Examples:

Input: Root of following BST
              5
            /   \
           2     13

Output: The given BST is converted to following Binary Tree
              18
            /   \
          20     13

Source: Convert a BST

Solution: Do reverse Inoorder traversal. Keep track of the sum of nodes visited so far. Let this sum be sum. For every node currently being visited, first add the key of this node to sum, i.e. sum = sum + node->key. Then change the key of current node to sum, i.e., node->key = sum.
When a BST is being traversed in reverse Inorder, for every key currently being visited, all keys that are already visited are all greater keys.
'''
#顺序。  right, root, left
#因为bst本身排好了序 。  所以就容易了很多
class Solution:
    def addGreater(self, root):
        self.s = 0
        self.dfs(root)

    def dfs(self, root):
        if not root: return
        self.dfs(root.right)
        self.s +=root.val
        root.val = self.s
        self.dfs(root.left)