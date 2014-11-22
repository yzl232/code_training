# encoding=utf-8
'''
Given a Binary Tree (balanced or not) write a method that transforms the tree in a degenerate tree (basically a data structure like a sorted linked list where each node has the left child null) and returns the new root. This must be made in place, no external memory usage is allowed.


就是leetcode原题。  最多加上sort linkedlist. (用merge sort)     普通的binary tree本身没有sort的属性。 所以没什么办法。 只好nlogn sort
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root: return
        left = root.left
        right = root.right

        if left:
            root.right = left
            root.left = None
            rightMost = left
            while rightMost.right:
                rightMost = rightMost.right
            rightMost.right = right
        self.flatten(root.right)

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

'''
flatten:     每次处理一个节点。 然后recursion
每次有三步：
1       左节点制空 root.left = None
2 root.right= left
3   rightMost.right = right
'''