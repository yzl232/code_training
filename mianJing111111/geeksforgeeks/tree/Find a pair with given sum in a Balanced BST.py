# encoding=utf-8
'''
Find a pair with given sum in a Balanced BST

Given a Balanced Binary Search Tree and a target sum, write a function that returns true if there is a pair with sum equals to target sum, otherwise return false. Expected time complexity is O(n) and only O(Logn) extra space can be used. 。


'''

class Solution:
    # @param root, a tree node  #注意这道题目不是binary search tree  。
    # @return nothing, do it in place  #他的顺序是   in order  left, root, right
    def flatten(self, root):  #我们反过来，就是right, root, left
        self.head = None
        self.dfs(root)

    def dfs(self, root):
        if not root: return
        self.dfs(root.right)
        if self.head:
            root.right = self.head  #右边连上
            self.head.left = root
        self.head = root    #更新head
        self.dfs(root.left)

class Solution3:
    def twoSum(self, head, tail, target):
        while head.val < tail.val:
            cur = head.val + tail.val
            if cur == target: return True
            elif cur<target:  head=head.next
            else: tail = tail.prev