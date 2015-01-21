# encoding=utf-8
'''
ertical Sum in a given Binary Tree

Given a Binary Tree, find vertical sum of the nodes that are in same vertical line. Print all sums through different vertical lines.

Examples:

      1
    /   \
  2      3
 / \    / \
4   5  6   7

The tree has 5 vertical lines

Vertical-Line-1 has only one node 4 => vertical sum is 4
Vertical-Line-2: has only one node 2=> vertical sum is 2
Vertical-Line-3: has three nodes: 1,5,6 => vertical sum is 1+5+6 = 12
Vertical-Line-4: has only one node 3 => vertical sum is 3
Vertical-Line-5: has only one node 7 => vertical sum is 7

So expected output is 4, 2, 12, 3 and 7
'''

class Solution:
    def findVertical(self, root):
        self.d = {}  #用hashtable是因为不知道最左边index有多左。
        self.dfs(root, 0)
        k1, k2 = min(self.d), max(self.d)
        return [self.d[x] for x in range(k1, k2+1)]

    def dfs(self, root,  colLevel):
        if not root: return
        if colLevel not in self.d:  self.d[colLevel] = 0
        self.d[colLevel]+=root.val
        self.dfs(root.left,colLevel-1)
        self.dfs(root.right,  colLevel+1)