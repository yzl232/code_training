# encoding=utf-8
'''


Clone a Binary Tree with Random Pointers

Given a Binary Tree where every node has following structure.

struct node {
    int key;
    struct node *left,*right,*random;
}

The random pointer points to any random node of the binary tree and can even point to NULL, clone the given binary tree.


Method 1 (Use Hashing)
The idea is to store mapping from given tree nodes to clone tre node in hashtable. Following are detailed steps.

1) Recursively traverse the given Binary and copy key value, left pointer and right pointer to clone tree. While copying, store the mapping from given tree node to clone tree node in a hashtable. In the following pseudo code, ‘cloneNode’ is currently visited node of clone tree and ‘treeNode’ is currently visited node of given tree.

   cloneNode->key  = treeNode->key
   cloneNode->left = treeNode->left
   cloneNode->right = treeNode->right
   map[treeNode] = cloneNode

2) Recursively traverse both trees and set random pointers using entries from hash table.

   cloneNode->random = map[treeNode->random]

和leetcode  list的题目类似。  hash或者临时改变结构

第二种是最优解。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.random = None

#简单的hashtable.   先全部复制。 然后对应连接
class Solution:
    def cloneTree(self, root):
        if not root:  return
        self.hashmap = {}
        self.copyNode(root)
        self.connect(root)     #和leetcode类似。 两步。 copy, connect
        return self.hashmap[root]

    def copyNode(self, root):
        if not root: return
        self.hashmap[root] = TreeNode(root.val)   #复制
        self.copyNode(root.left)
        self.copyNode(root.right)

    def connect(self, root):
        if not root: return
        tmp = self.hashmap[root]
        if root.left:   tmp.left = self.hashmap[root.left]  #connect
        if root.right:  tmp.right = self.hashmap[root.right]
        if root.random:  tmp.random = self.hashmap[root.random]
        self.connect(root.left)
        self.connect(root.right)

#最优解
class Solution3:
    def cloneTree(self, root): #和leetcode 类似。 三步 copy, connect ，restore
        if not root: return    #都复制到原本的left
        root1 = self.copyLRNode(root)
        self.copyRandom(root, root1)
        self.restore(root, root1)
        return root1

    def copyLRNode(self, root):
        if not root: return
        left = root.left
        root.left = TreeNode(root.val)
        root.left.left = left
        if root.left: self.copyLRNode(left)
        if root.right:  root.left.right = self.copyLRNode(root.right)
        return root.left

    def copyRandom(self, root, root1):
        if not root: return
        if root.random: root1.random = root.random.left
        if root1.left:  self.copyRandom(root1.left, root1.left.left)
        if root1.right: self.copyRandom(root.right, root1.right)

    def restore(self, root, root1):
        if not root: return
        if root1.left:
            root.left = root1.left
            root1.left = root1.left.left
        else:   root.left = None
        self.restore(root.left, root1.left)
        self.restore(root.right, root1.right)