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


#和leetcode都一样。
hashmap:  1 复制node  2 连接random
最优解： 1 复制node并插入  2 连接 random  3 断开

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
        self.d = {None:None} #处理空值的情况
        self.copyNode(root)
        self.connect(root)     #和leetcode类似。 两步。 copy, connect
        return self.d[root]

    def copyNode(self, root):
        if not root: return
        self.d[root] = TreeNode(root.val)   #复制
        self.copyNode(root.left)
        self.copyNode(root.right)

    def connect(self, root):
        if not root: return
        t = self.d[root]
        t.left = self.d[root.left]  #connect
        t.right = self.d[root.right]
        t.random = self.d[root.random]
        self.connect(root.left)
        self.connect(root.right)

#最优解
class Solution3:
    def cloneTree(self, root): #和leetcode 类似。 三步 copy, connect ，restore
        if not root: return    #都复制到原本的left
        root1 = self.copyInsert(root)
        self.connectRandom(root, root1)
        self.restore(root, root1)
        return root1

    def copyInsert(self, root):
        if not root: return
        left = root.left  #因为root存到left的位置， 所以要暂存left
        r1 = TreeNode(root.val)
        root.left = r1
        r1.left = self.copyInsert(left)      #其实可以不用if判断
        r1.right = self.copyInsert(root.right)
        return r1

    def connectRandom(self, root, r1):
        if not root: return
        if root.random: r1.random = root.random.left  #这个if还是必须有的。
        if r1.left:  self.connectRandom(r1.left, r1.left.left)  #这里注意了！！！！ 必须有这个if
        self.connectRandom(root.right, r1.right)

    def restore(self, root, r1):
        if not root: return
        if r1.left:     #这个if还是必须有的。
            root.left = r1.left
            r1.left = r1.left.left
        else:   root.left = None  #必须制空
        self.restore(root.left, r1.left)
        self.restore(root.right, r1.right)