# encoding=utf-8
'''

Print Nodes in Top View of Binary Tree

Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. Given a binary tree, print the top view of it. The output nodes can be printed in any order. Expected time complexity is O(n)

A node x is there in output if x is the topmost node at its horizontal distance. Horizontal distance of a child of a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.

       1
    /     \
   2       3
  /  \    / \
 4    5  6   7

 简单的说，就是column形式的view。每个colum取顶端一个。
Top view of the above binary tree is
4 2 1 3 7

        1
      /   \
    2       3
      \
        4
          \
            5
             \
               6
Top view of the above binary tree is
2 1 3 6

基本上和vertical  columns一模一样。
'''
#hashmap值同时也存lvl的值
# top view是最难的。 同时要rlvl, clvl

class Solution:
    def findVertical(self, root):
        self.d = {}  #用hashtable是因为不知道最左边index有多左。
        self.dfs(root, 0,  0)
        k1 = min(self.d); k2 = max(self.d)
        return [min(self.d[x])[-1] for x in range(k1, k2+1)]

    def dfs(self, root, rlvl,  clvl):
        if not root: return
        if clvl not in self.d:  self.d[clvl] = []
        self.d[clvl].append((rlvl, root.val))
        self.dfs(root.left,rlvl+1,  clvl-1)
        self.dfs(root.right, rlvl+1,  clvl+1)

'''
class Solution:
    def findVertical(self, root):
        self.d = {}  #用hashtable是因为不知道最左边index有多左。
        self.dfs(root, 0,  0)
        result = []
        for key in sorted(self.d):
            top = min(self.d[key])
            result.append(top[-1])
        return result

    def dfs(self, root, rlvl,  clvl):
        if not root: return
        if clvl not in self.d:  self.d[clvl] = []
        self.d[clvl].append((rlvl, root.val))
        self.dfs(root.left,rlvl+1,  clvl-1)
        self.dfs(root.right, rlvl+1,  clvl+1)
'''



'''
geeks的做法时间复杂度比较高。
我这个耗费空间。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t1.left = t2
t1.right = t3
t2.right = t4
t4.right = t5
t5.right = t6

s = Solution()
print s.findVertical(t1)