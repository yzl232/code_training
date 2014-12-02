# encoding=utf-8
'''
Binary Tree to Binary Search Tree Conversion

转化成array， 再sort，  再转化

转化成single linked list, 然后sort， 然后recover

也就是3个leetcode    linked list的
'''

class Solution1:
    # @param root, a tree node  #注意这道题目不是binary search tree  。  是类似heap
    # @return nothing, do it in place  #他的顺序是   inorder的顺序。    root, left, right.
    def flatten(self, root):  #我们反过来，就是right, left, root
        self.head = None
        self.dfs(root)

    def dfs(self, root):
        if not root: return
        self.dfs(root.right)
        self.dfs(root.left)
        root.right = self.head  #右边连上
        root.left = None  #左置空
        self.head = root    #更新head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution5:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next: return head
        fast = slow = head
        while fast.next and fast.next.next:  #因为要对前面的节点进行裂开操作。 着了是 fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(head2)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1); cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

class Solution9:
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