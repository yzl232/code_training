# encoding=utf-8
'''
how to merge two binary search tree into balanced binary search tree.. Let there be m elements in first tree and n elements in the other tree. Your merge function should take O(m+n) time with in constant space.

Examples:


A Balanced BST 1
90
/ \
70 110


A Balanced BST 2

60
/ \
5 800

output :-->
70
/ \
60 90
/ \
5 800



This can be done in 3 steps:
1. covert the BSTs to sorted linked list (this can be done in place with O(m+n) time)

2. Merge this two sorted linked lists to a single list (this can be done in place with O(m+n) time)

3. Convert sorted linked list to balanced BST (this can be done in place with O(m+n) time)

基本上都是leetcode  3道题目综合来搞定
'''
class Solution1:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.head = None
        self.dfs(root)

    def dfs(self, root):
        if not root: return
        self.dfs(root.right)
        root.right = self.head  #右边连上
        root.left = None  #左置空
        self.head = root    #更新head
        self.dfs(root.left)


class Solution5:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        prev = dummy
        while l1 and l2:
            if l1.val > l2.val:
                prev.next = l2
                l2=l2.next
            else:
                prev.next = l1
                l1 = l1.next
            prev = prev.next
        if l1:prev.next = l1
        elif l2:prev.next = l2
        return dummy.next

class Solution2:
    head = None
    def sortedListToBST(self, head):
        current, length = head, 0
        while current != None:
            current, length = current.next, length + 1
        self.head = head
        return self.sortedRecur(0, length - 1)

    def sortedRecur(self, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        left = self.sortedRecur(start, mid - 1)
        root = TreeNode(self.head.val)
        root.left = left
        self.head = self.head.next
        root.right = self.sortedRecur(mid + 1, end)
        return root