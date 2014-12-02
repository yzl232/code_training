# encoding=utf-8
'''
Alternating split of a given Singly Linked List

Write a function AlternatingSplit() that takes one list and divides up its nodes to make two smaller lists ‘a’ and ‘b’. The sublists should be made from alternating elements in the original list. So if the original list is 0->1->0->1->0->1 then one sublist should be 0->0->0 and the other should be 1->1->1.





Question is to split the list into two parts. We are supposed to modify the original list by modifying its next pointers. Do we have to use double pointers for this. Here's a code that splits the list using only two pointers in a recursive manner.

有个留言的哥们，解法牛逼。用recursion


'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitAl(self, head):
        if not head: return
        self.recur(head, head.next)

    def recur(self, head1, head2):
        if not head1 or not head2: return
        if head1.next:  head1.next = head1.next.next
        if head2.next: head2.next = head2.next.next
        self.recur(head1.next, head2.next)