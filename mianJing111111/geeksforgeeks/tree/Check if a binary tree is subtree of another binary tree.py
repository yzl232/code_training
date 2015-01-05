# encoding=utf-8
'''
Check if a binary tree is subtree of another binary tree | Set 1

Given two binary trees, check if the first tree is subtree of the second one. A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T.


The subtree corresponding to the root node is the entire tree; the subtree corresponding to any other node is called a proper subtree.

For example, in the following case, tree S is a subtree of tree T.

        Tree S
          10
        /    \
      4       6
       \
        30


        Tree T
              26
            /   \
          10     3
        /    \     \
      4       6      3
       \
        30

Solution: Traverse the tree T in preorder fashion. For every visited node in the traversal, see if the subtree rooted with this node is identical to S.


We have discussed a O(n2) solution for this problem. In this post a O(n) solution is discussed. The idea is based on the fact that inorder and preorder/postorder uniquely identify a binary tree. Tree S is a subtree of T if both inorder and preorder traversals of S arew substrings of inorder and preorder traversals of T respectively.

Following are detailed steps.

1) Find inorder and preorder traversals of T, store them in two auxiliary arrays inT[] and preT[].

2) Find inorder and preorder traversals of S, store them in two auxiliary arrays inS[] and preS[].

3) If inS[] is a subarray of inT[] and preS[] is a subarray preT[], then S is a subtree of T. Else not.

We can also use postorder traversal in place of preorder in the above algorithm.

Let us consider the above example

Inorder and Preorder traversals of the big tree are.
inT[]   =  {a, c, x, b, z, e, k}
preT[]  =  {z, x, a, c, b, e, k}

Inorder and Preorder traversals of small tree are
inS[]  = {a, c, x, b}
preS[] = {x, a, c, b}

We can easily figure out that inS[] is a subarray of
inT[] and preS[] is a subarray of preT[].

EDIT

The above algorithm doesn't work for cases where a tree is present
in another tree, but not as a subtree. Consider the following example.

        Tree1
          x
        /    \
      a       b
     /
    c


        Tree2
          x
        /    \
      a       b
     /         \
    c            d

Inorder and Preorder traversals of the big tree or Tree2 are.

Inorder and Preorder traversals of small tree or Tree1 are

The Tree2 is not a subtree of Tree1, but inS[] and preS[] are
subarrays of inT[] and preT[] respectively.

The above algorithm can be extended to handle such cases by adding a special character whenever we encounter NULL in inorder and preorder traversals. Thanks to Shivam Goel for suggesting this extension.
'''
#本来只用serialization来做。 发现不行。  subtree必须包括all of its descendants。   serialize可能只有一小部分
#然后必须用preorder+inorder+serialization



class Solution:  #O(n)
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, a, small):
        self.inResult = []; self.preResult = []
        self.inorder(a); self.preorder(a)
        aIn = self.inResult[:]; aPre = self.preResult[:]
        self.inResult =[]; self.preResult=[]
        self.inorder(small); self.preorder(small)
        return self.inResult in aIn and self.preResult in aPre

    def inorder(self, root):
        if not root:
            self.inResult.append('#')
            return

        self.inorder(root.left)
        self.inResult.append(root.val)
        self.inorder(root.right)

    def preorder(self, root):
        if not root:
            self.preResult.append('#')
            return
        self.preResult.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)




class Solution92:  #效率不高的做法  O(n2)
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):  #和symmitric tree题目一模一样
        if not p and not q: return  True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubTree(self, a, small):
        if not small: return True
        if not a: return False
        if self.isSameTree(a, small): return True
        return self.isSubTree(a.left, small) or self.isSubTree(a.right, small)

#用递归来做，都是特殊case加上recursion


#G家题目
'''
给一个二叉树，让找出所有相同的子树。
'''
