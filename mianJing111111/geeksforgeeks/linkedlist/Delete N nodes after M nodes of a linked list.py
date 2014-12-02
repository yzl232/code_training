# encoding=utf-8
'''


Delete N nodes after M nodes of a linked list

Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.

Difficulty Level: Rookie

Examples:

Input:
M = 2, N = 2
Linked List: 1->2->3->4->5->6->7->8
Output:
Linked List: 1->2->5->6
'''
class Solution:
    def skipMdeleteN(self, head, m, n):
        if not head or not head.next: return
        cur = head
        for i in range(m-1):
            if cur: cur = cur.next
        if not cur: return
        t = cur.next
        for i in range(n):
            if t: t = t.next
        cur.next = t
        self.skipMdeleteN(t, m, n)