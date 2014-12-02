# encoding=utf-8
'''
Difficulty Level: Rookie
Write a C function to insert a new value in a sorted Circular Linked List (CLL). For example, if the input CLL is following.


存一个tail会更方便
Instead of having a pointer to head node in circular linked it is more convenient to maintain pointer to the last node because then we can have pointer to the last node as well as the first node. Or in other words :
head = tail->next;
Benifits :
- so inserting at the beginning does not require moving in a loop for n times to the find the pointer to last node, n being the length of the linked list.


三种情况：
1) Linked List is empty:
2) New node is to be inserted just before the head node:
3) New node is to be  inserted somewhere after the head:

'''
class Solution: #return head
    def insrt(self, head, node):
        if not head:   return node
        cur = head
        while cur.next != head:  cur = cur.next
        tail = cur
        if node.val <= head.val:  #tail也要连上circular
            node.next = head
            tail.next = node
            return node
        else:
            cur = head
            while cur.next != head and cur.next.val<node.val:
                cur = cur.next
            node.next = cur.next
            cur.next = node
            return head