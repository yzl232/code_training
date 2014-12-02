# encoding=utf-8
'''

Print all nodes that are at distance k from any leaf node

Given a Binary Tree and a positive integer k, print all nodes that are distance k from a leaf node.

Here the meaning of distance is different from previous post. Here k distance from a leaf means k levels higher than a leaf node. For example if k is more than height of Binary Tree, then nothing should be printed. Expected time complexity is O(n) where n is the number nodes in the given Binary Tree.

和之前那个比较难的distance k from a given node又是大不一样的。
并且本身不能是leaf。 是所有距离任意leaf距离为k的非leaf的节点


The idea is to traverse the tree. Keep storing all ancestors till we hit a leaf node. When we reach a leaf node, we print the ancestor at distance k. We also need to keep track of nodes that are already printed as output. For that we use a boolean array visited[]

保存所有的ancestor， 也就是path.  然后从path反向数数

'''
class Solution:
    def findK(self, root, k):
        self.result = set([])
        self.k = k
        self.dfs(root, [])
        return self.result

    def dfs(self, root, path):
        if not root:  return [0]
        if not root.left and not root.right:
            if len(path)>self.k:   self.result.add(path[-self.k])
        l = self.dfs(root.left, path+[root.val])
        r = self.dfs(root.right, path+[root.val])
        return min(l, r)+1