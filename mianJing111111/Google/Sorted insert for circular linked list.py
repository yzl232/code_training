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


#Google 考过类似。  Double Circular Sorted Linked List Insert
# 尾部的判定不是x！=None。 而是x！= h
# 前2种特殊情况return都是x
class Solution: #return head
    def insrt(self, h, x):  #circular就是都要注意尾巴的连接。
        if not h:
            x.next = x
            return x
        if x.val <=h.val:
            tail = h
            while tail.next != h:  tail = tail.next  #找tail
            tail.next = x;  x.next = h
            return x
        else:
            pre = h
            while pre.next != h and pre.next.val<x.val:   pre = pre.next
            x.next = pre.next  # 逻辑。连环
            pre.next = x
            return h


#G家
'''
Double Circular Sorted Linked List Insert
区别不大。 一个是找tail用pre就可以找了。 一个是要注意更新pre节点。
'''
class Solution: #return head
    def insrt(self, h, x):  #circular就是要注意尾巴的连接
        if not h:
            x.next = x
            x.pre = x
            return x
        if x.val <=h.val:
            tail = h.pre  #找tail
            x.next = h; h.pre = x   #前后的逻辑
            x.pre = tail; tail.next = x
            return x
        else:
            pre = h
            while pre.next != h and pre.next.val<x.val:    pre = pre.next
            nextN = pre.next
            x.next = nextN; nextN.pre = x
            pre.next = x; x.pre = pre
            return h