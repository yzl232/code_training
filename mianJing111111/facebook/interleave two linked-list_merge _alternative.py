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
        h=l1
        while l1 and l2:   #每次只处理一个node
            t1 = l1.next;   t2 = l2.next
            l1.next = l2;   l2.next = t1
            l1 = t1;   l2 = t2
        return h