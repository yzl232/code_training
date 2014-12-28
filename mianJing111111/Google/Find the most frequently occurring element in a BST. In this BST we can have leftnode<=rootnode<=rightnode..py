# encoding=utf-8
'''
Find the most frequently occurring element in a BST. In this BST we can have leftnode<=rootnode<=rightnode.
'''
#. If we traverse this BST with Inorder, we can consider this is sorted array. Then we can get the most frequent node in [ Time : O(n), Space : O(1) ].

#hashmap更简单。  space更多一些。

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        self.retCn=self.curCnt=0
        self.preV=self.ret=None
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root:    return
        self.dfs(root.left)
        if root.val != self.preV:
            self.curCnt=0
            self.preV = root.val
        self.curCnt+=1
        if self.curCnt>self.retCnt:
            self.retCnt = self.curCnt
            self.ret = root.val
        self.dfs(root.right)