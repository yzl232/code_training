# encoding=utf-8
'''
Alternating split of a given Singly Linked List

Write a function AlternatingSplit() that takes one list and divides up its nodes to make two smaller lists ‘a’ and ‘b’. The sublists should be made from alternating elements in the original list. So if the original list is 0->1->0->1->0->1 then one sublist should be 0->0->0 and the other should be 1->1->1.





Question is to split the list into two parts. We are supposed to modify the original list by modifying its next pointers. Do we have to use double pointers for this. Here's a code that splits the list using only two pointers in a recursive manner.

有个留言的哥们，解法牛逼。用recursion


'''
class ListNode:    #背下 h2.next = h2.next.next  就可以了
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitAl(self, h):
        if not h: raise ValueError()
        ret = (h, h.next)
        self.help(h, h.next)
        return ret

    def help(self, h1, h2):
        if not h1 or not h2: return
        if h1.next:  h1.next = h1.next.next
        if h2.next: h2.next = h2.next.next
        self.help(h1.next, h2.next)


'''
# clone list with random node 用到了
class Solution:
    def splitAl(self, h):
        cur = h
        h2 = h.next
        while cur:  # choose next pointers . decouple the list
            t = cur.next
            cur.next = t.next
            if t.next:   t.next = t.next.next     # 1, 2, 3, (4)  .   1=3,  2=4
            cur = cur.next
        return h2
'''