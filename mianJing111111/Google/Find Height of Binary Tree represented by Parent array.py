# encoding=utf-8
'''

Find Height of Binary Tree represented by Parent array

A given array represents a tree in such a way that the array value gives the parent node of that particular index. The value of the root node index would always be -1. Find the height of the tree.
Height of a Binary Tree is number of nodes on the path from root to the deepest leaf node, the number includes both root and leaf.

Input: parent[] = {1 5 5 2 2 -1 3}
Output: 4
The given array represents following Binary Tree
         5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6

利用index来标记的。  index是值。
值表示parent的值。

Input: parent[] = {-1, 0, 0, 1, 1, 3, 5};
Output: 5
The given array represents following Binary Tree
         0
       /   \
      1     2
     / \
    3   4
   /
  5
 /
6



方法一： 重建树。
The tree can be constructed recursively by first searching the current root, then recurring for the found indexes and making them left and right subtrees of root. This solution takes O(n2) as we have to linearly search for every node.


'''

#考虑一个n叉树，将所有node存在一个数组tree中，node编号从0到n(n为数组大小)
#。 arr[i]表示第i个node的parent，请找出该树的深度(即最长的根到叶的路径长度)
# G家考过
# O(n)的做法并不在乎是不是N叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#方法一。重建树.   BFS.  O(n2)
#利用index来标记的。  index是值。
#值表示parent的值。
class Solution:
    def restore(self, arr): #与标准level order区别就是在arr找index。 以及每次在arr置None
        i = arr.index(-1)  #看看就好
        root = TreeNode(i)
        arr[i]=None
        pre = [root]
        while pre:
            cur = []
            for node in pre:
                if node.val in arr:
                    i =arr.index(node.val)
                    left = TreeNode(i)
                    node.left = left
                    arr[i] = None
                    cur.append(left)
                if node.val in arr:
                    i =arr.index(node.val)
                    right = TreeNode(i)
                    node.right = right
                    arr[i]=None
                    cur.append(right)
            pre = cur
        return root

# O(n)
class Solution:
    def findHeight(self, arr):
        self.depth = {}
        self.arr = arr
        for i in range(len(arr)):    self.fill(i)
        return max(self.depth.values())

    def fill(self, i):
        if i in self.depth: return   #已经fill
        parent = self.arr[i]
        if parent == -1:
            self.depth[i] = 1;  return
        self.fill(parent)
        self.depth[i] = self.depth[parent]+1   #parent深度+1
#非常的巧妙
# 递归形式的dp。类似于 memoization