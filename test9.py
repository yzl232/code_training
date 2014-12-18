'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0; dummy = ListNode(0); cur = dummy
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry, s= s/10, s%10
            cur.next = ListNode(s)
            l1 = l1.next; l2 = l2.next; cur = cur.next
        while l1:
            s = l1.val+ carry
            carry, s= s/10, s%10
            cur.next = ListNode(s)
            cur = cur.next; l1 = l1.next
        while l2:
            s = l2.val + carry
            carry, s= s/10, s%10
            cur.next = ListNode(s)
            cur = cur.next; l2 = l2.next
        if carry:    cur.next = ListNode(1)
        return dummy.next