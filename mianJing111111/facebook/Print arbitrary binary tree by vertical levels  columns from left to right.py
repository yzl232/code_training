# encoding=utf-8
'''
We have a binary tree, suppose like this:

       8
     /   \
    6     10
   / \   /  \
  4   7 9    12
 / \
3   5

We have to print this binary tree in top-down manner - column wise. Note that, 8, 7 & 9 would be considered in same column. So the required output should be:

3
4
6 5
8 7 9
10
12


必须是先left, root, right


注意8, 7, 9的顺序。 必须用pre order

'''
#可以看出，注意8, 7, 9的顺序，  是inorder, root,   left, ，  right
class Solution:
    def findVertical(self, root):
        self.d = {}  #用hashtable是因为不知道最左边index有多左。
        self.dfs(root, 0)
        result = []
        for key in sorted(self.d):
            result.append(self.d[key])
        return result

    def dfs(self, root,  colLevel):
        if not root: return
        if colLevel not in self.d:  self.d[colLevel] = [] ##可以看出，注意8, 7, 9的顺序，  是inorder, root,   left, ，  right
        self.d[colLevel].append((root.val))
        self.dfs(root.left,colLevel-1)
        self.dfs(root.right,  colLevel+1)




'''
geeks的做法时间复杂度比较高。
我这个耗费空间。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1 = TreeNode(8)
t2 = TreeNode(6)
t3 = TreeNode(10)
t4 = TreeNode(7)
t5 = TreeNode(9)
t6 = TreeNode(6)
t1.left = t2
t1.right = t3
t2.right = t4
t3.left = t5

s = Solution()
print s.findVertical(t1)