# encoding=utf-8
'''
Function to check if a singly linked list is palindrome

分成两半。  reverse后半
'''
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next: return head
        fast = slow = head
        while fast.next and fast.next.next:  #因为要对前面的节点进行裂开操作。 着了是 fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        head2 = self.reverse(head2)
        while head and head2:  #其中某个可能会长一点点。 无所谓
            if head.val !=head2.val: return False
            head=head.next
            head2=head2.next
        return True

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