# encoding=utf-8
# reverse a linked list

'''
There can be various methods to reverse a linked list, but here we can take advantage of it being a doubly linked list:

1. loop from head to tail. For each node swap next and prev.

for(p = head;p!=NULL;p=r)
{
r=p->next;
p->next=p->next^p->prev;
p->prev=p->next^p->prev;
p->next=p->next^p->prev;
}

2.swap head and tail.
'''

class Solution2:
    def reverse(self, head):    #更简单一些。因为有pre, next。 不需要last, pre
        while head:
            head.pre, head.next = head.next, head.pre
            if not head.pre: break  # finished         #因为没有do while。 所以只能这样写
            head=head.pre #本来是next. 调换了。
        return head



#single linked list
class Solution:
    def reverse(self, head):
        if not head: return
        dummy= ListNode(0); dummy.next=  head
        pre, last, cur = dummy, head, head.next
        while cur:  #last一直是最后一个。 不变。
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next   #四层的封闭连环
        return dummy.next