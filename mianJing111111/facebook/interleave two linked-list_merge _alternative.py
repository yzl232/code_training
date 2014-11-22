# encoding=utf-8
'''
interleave two linked-list

1  3  5
2  4  6

123456

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        prev = dummy
        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2
        return dummy.next