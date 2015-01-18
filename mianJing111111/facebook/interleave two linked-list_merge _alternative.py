# encoding=utf-8
'''
interleave two linked-list

1  3  5
2  4  6

123456


Merge a linked list into another linked list at alternate positions

Given two linked lists, insert nodes of second list into first list at alternate positions of first list.

For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6,
the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty.

The nodes of second list should only be inserted when there are positions available. F

or example, if the first list is 1->2->3 and second list is 4->5->6->7->8,
 then first list should become 1->4->2->5->3->6 and second list to 7->8.

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
    def mergeTwoLists(self, l1, l2):   #很多corner case没有考虑
        h1=l1; h2=l2
        while l1 and l2:   #每次只处理一个node
            t1 , t2 =l1.next,  l2.next
            l1.next , l2.next =l2,  t1
            l1, l2 = t1,  t2
        return h1, h2