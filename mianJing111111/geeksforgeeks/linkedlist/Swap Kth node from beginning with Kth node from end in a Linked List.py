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
        p1 = p2 = None  #p1, p2记录以前的位置
        dummy = ListNode(0); dummy.next = head
        cur = dummy;  cnt = 0
        while cur.next:
            if cnt==k-1:  #例子 1-2-3   k=2
                p1 = cur
                p2 = dummy
            elif cnt>k-1:  #保证了p2走 n-k步
                p2 = p2.next
            cur = cur.next
            cnt+=1
        if cnt<k: return  #因为加上了dummy. cnt-1
        if p1 and p1.next and p2 and p2.next:
            tmp1 = p1.next.next
            tmp2 = p2.next.next
            p1.next, p2.next = p2.next, p1.next
            p1.next.next = tmp1
            p2.next.next = tmp2