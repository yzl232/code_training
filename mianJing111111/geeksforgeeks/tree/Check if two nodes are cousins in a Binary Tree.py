# encoding=utf-8
'''

Check if two nodes are cousins in a Binary Tree

Given the binary Tree and the two nodes say ‘a’ and ‘b’, determine whether the two nodes are cousins of each other or not.

Two nodes are cousins of each other if they are at same level and have different parents.

Example

     6
   /   \
  3     5
 / \   / \
7   8 1   3
Say two node be 7 and 1, result is TRUE.
Say two nodes are 3 and 5, result is FALSE.
Say two nodes are 7 and 5, result is FALSE.

We strongly recommend to minimize the browser and try this yourself first.

The idea is to find level of one of the nodes. Using the found level, check if ‘a’ and ‘b’ are at this level. If ‘a’ and ‘b’ are at given level, then finally check if they are not children of same parent.


#看定义描述。 一:同一层。 二：不是同一parent

Time Complexity of the above solution is O(n) as it does at most three traversals of binary tree.

'''
#一般都是分成2个部分分别作。 一般做不到并在一起
#树都是这样子。2种特殊情况，然后一种是root为空。  一种是考虑root值。
class Solution:
    def isSibling(self, root, a, b): #cousin比较难检查。 但是反过来，sibling很好检查
        if not root: return False
        if (root.left, root.right) in [(a, b), (b,a)]: return True
        return self.isSibling(root.left, a, b) or self.isSibling(root.right, a, b)   #寻找一个root， 左右subling是a, b

    def findLevel(self, root, node):
        self.ret = None; self.node = node
        self.dfs(root, 1)
        return self.ret

    def dfs(self, root, level): #找一个子节点到root得距离
        if self.ret !=None: return 
        if not root: return
        if self.ret: return
        if root == self.node:     self.ret = level
        self.dfs(root.left, level+1)
        self.dfs(root.right,  level+1)

    def isCousin(self, root, a, b):
        if not a or not b: raise ValueError
        return self.findLevel(root, a) == self.findLevel(root, b) and not (self.isSibling(root, a, b))  #总共traverse 3 次   O(n)

'''
    def level(self, root, p, lvl):  #实际上是一个search的过程
        if not root: return -1  #特殊情况： 没找到
        if root == p: return lvl  #特殊情况：  找到
        l = self.level(root.left, p, lvl+1)  #和distance 蛮像的
        if l!=-1: return l
        return self.level(root.right, p, lvl+1)

'''
