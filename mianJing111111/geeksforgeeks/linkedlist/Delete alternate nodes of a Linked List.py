# encoding=utf-8
'''

Delete alternate nodes of a Linked List

Given a Singly Linked List, starting from the second node delete all alternate nodes of it. For example, if the given linked list is 1->2->3->4->5 then your function should convert it to 1->3->5, and if the given linked list is 1->2->3->4 then convert it to 1->3.

python有垃圾回收，不用考虑垃圾回收

有iterative还有recursion两种。
'''
class Solution:
    def delAl(self, h):
        if not h: return
        if h.next:  h.next = h.next.next
        self.delAl(h.next)