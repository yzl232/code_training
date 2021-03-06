# encoding=utf-8
'''
print all nodes at distance k from a given node

Given a binary tree, a target node in the binary tree, and an integer value k, print all the nodes that are at distance k from the given target node. No parent pointers are available.

BinaryTree

Consider the tree shown in diagram

Input: target = pointer to node with data 8.
       root = pointer to node with data 20.
       k = 2.
Output : 10 14 22

If target is 14 and k is 3, then output
should be "4 20"


We strongly recommend to minimize the browser and try this yourself first.

There are two types of nodes to be considered.
1) Nodes in the subtree rooted with target node. For example if the target node is 8 and k is 2, then such nodes are 10 and 14.
第一类简单。

2) Other nodes, may be an ancestor of target, or a node in some other subtree. For target node 8 and k is 2, the node 22 comes in this category.



Finding the first type of nodes is easy to implement. Just traverse subtrees rooted with the target node and decrement k in recursive call. When the k becomes 0, print the node currently being traversed (See this for more details). Here we call the function as printkdistanceNodeDown().

How to find nodes of second type? For the output nodes not lying in the subtree with the target node as the root, we must go through all ancestors. For every ancestor, we find its distance from target node, let the distance be d, now we go to other subtree (if target was found in left subtree, then we go to right subtree and vice versa) of the ancestor and find all nodes at k-d distance from the ancestor.
'''
#来自   Print nodes at k distance from root

#太难了。 决定放弃此题。

class Solution:
    def findKDist(self, root, target, k):
        self.ret =[]
        self.down(target, k)  #从target往下搜。
        self.up(root, target, k)
        return self.ret

    def down(self, root ,k):
        if not root: return
        if k==0:
            self.ret.append(root.val)
            return
        self.down(root.left, k-1)
        self.down(root.right, k-1)
#一个是求lvl。一个是已知lvl，求node
    def up(self, root, target, k):  #做法和ancestor非常像.  基本上一样的套路.findLvl扩展
        if not root: return -1  #没找到
        if root == target: return 0  #找到了
        n1 = self.up(root.left, target, k)  #target要么在n1, 要么在n2
        if n1 !=-1:  #Check if target node was found in left subtree
            if (n1+1)==k:  self.ret.append(root.val)  #左子树是n1,  parent是n1+1
            else:  self.down(root.right, k-n1-2)    #右子树是n1+2.      n1+1<k
            return 1+n1
        n2 = self.up(root.right, target, k)
        if n2!=-1:
            if (n2+1)==k: self.ret.append(root.val)
            else:  self.down(root.left, k-n2-2)  #每次都必须同时检查右边
            return 1+n2    #每次往上， 加1，
        return -1  # If target was neither present in left nor in right subtree


#比较一下  find level:
    def findLevel(self, root, node, level): #找一个子节点到root得距离
        if not root: return -1  #没找到，就是-1
        if root == node: return level
        d = self.findLevel(root.left, level+1)
        if d !=-1: return d
        return self.findLevel(root.right,  level+1)
#下面次啊是findLevel最好的办法
'''
#shortest path 里面有用到。
class Solution:
    def findLevel(self, root, node):
        self.ret = None; self.node = node
        self.dfs(root, 1)
        return self.ret

    def dfs(self, root, level): #找一个子节点到root得距离
        if not root: return
        if self.ret: return
        if root == self.node:     self.ret = level
        self.dfs(root.left, level+1)
        self.dfs(root.right,  level+1)
'''