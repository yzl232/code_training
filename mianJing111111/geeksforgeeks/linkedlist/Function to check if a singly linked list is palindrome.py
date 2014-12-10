# encoding=utf-8
'''
Function to check if a singly linked list is palindrome

分成两半。  reverse后半
'''
class Solution:
    def isPalindrome(self, h):
        if not h or not h.next: return h
        fast = slow = h
        while fast.next and fast.next.next:  #因为要对前面的节点进行裂开操作。 着了是 fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        h2 = slow.next
        h2 = self.reverse(h2)
        while h and h2:  #其中某个可能会长一点点。 无所谓
            if h.val !=h2.val: return False
            h=h.next;    h2=h2.next
        return True

    def reverse(self, h):
        if not h: return
        dummy= ListNode(0); dummy.next=  h
        pre, last, cur = dummy, h, h.next
        while cur:  #last一直是最后一个。 不变。
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next   #四层的封闭连环
        return dummy.next