# encoding=utf-8
'''
Given a singly linked list, swap kth node from beginning with kth node from end. Swapping of data is not allowed, only pointers should be changed. This requirement may be logical in many situations where the linked list data part is huge (For example student details line Name, RollNo, Address, ..etc). The pointers are always fixed (4 bytes for most of the compilers).


参照leetcode    Remove Nth Node From End of List.

这肯定是要求one pass的解法。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapKth(self, head, k):
        p1 = p2 = None
        dummy = ListNode(0); dummy.next = head
        p3 = dummy;  cout = 1
        while p3.next:
            if cout==k:  #例子 1-2-3   k=2
                p1 = p3
                p2 = dummy
            elif cout>k:  #保证了p2走 n-k步
                p2 = p2.next
            p3 = p3.next
            cout+=1
        if cout-1<k: return
        if p1 and p1.next and p2 and p2.next:
            tmp1 = p1.next.next
            tmp2 = p2.next.next
            p1.next, p2.next = p2.next, p1.next
            p1.next.next = tmp1
            p2.next.next = tmp2