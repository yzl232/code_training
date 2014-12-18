# encoding=utf-8
'''
Given two extremely large numbers - each number is stored in a Singly Linked list, with the MSB at the head. You are not allowed to reverse the Linked lists. Write a program to multiply them in optimum space and time.

#加法很简单的。  这里是乘法。 很难。

least significant bit (LSB) and most significant bit (MSB)

Save the result in a doubly linked list:

#简单的做法是traverse， 然后得到2个数。 然后相乘。 然后建立一个新的list.


例子   1=>2=>5
                8=>0
    1=>0=>0=>0=>0





5->6->3 Multiplied by 8->4->2

Normal Multiplication:

      563
   *  842
---------------
      1126
     2252
    4504
----------------
    474046
----------------


O(m*n)


Now reverse both linked lists to access digits from right side..
3->6->5 , 2->4->8
Now multiply 3->6->5 with 2 we get
3*2 = 6, 6*2 = 12, 5*2 = 10
if number is not one digit then store it in carry add it to next number i.e,
after multiplying
3->6->5 with 2 ===> 6, carry = 0.
3->6->5 with 2 ===> 6->2, carry = 1.
3->6->5 with 2 ===> 6->2->1, carry = 1.
3->6->5 with 2 ===> 6->2->1->1, carry = 0.
Final result after multiplying single digit is 6->2->1->1
similarly 3->6->5 with 4 is 2->5->2->2
Now add the above two one directly and other with adding a single 0 at starting i.e, 6->2->1->1 + 0->2->5->2->2 = 6->4->6->3->2
Now again multiply 3->6->5 with 8 is 4->0->5->4 and add two 0's at starting so it will become 0->0->4->0->5->4

result will be 6->4->6->3->2 + 0->0->4->0->5->4 = 6->4->0->4->7->4
Now reverse that you will get final result : 4->7->4->0->4->6 Read more at: http://www.queryhome.com/18855/multiply-two-numbers-represented-by-linked-lists

这道题目难度太大。 看懂乘法的式子就好。

'''
#leetcode那个是逆转了。 从低位到高位。  不能逆转，可以改成double linked list.  用
#如果可以用extra space。 存到array里边








'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def multiply(self, node1, val, outNode):
        if not node1: return 0
        if val==0: return 0
        node1 = self.reverse(node1)
        dummy = ListNode(0);  dummy.next =  carry = 0; cur = dummy
        while cur:
            product = cur.val * val + carry
            carry = product/10
            cur.val = product%10
            cur = cur.next
        if carry:  cur.next = ListNode(carry)
        return self.reverse(dummy.next)

    def calCulateMultiply(self, n1, n2):
        if not n2 or not n1: return 0
        n2 = self.reverse(n2)
        h = self.multiply(n1, n2.val)
        n2 = n2.next
        while n2:
            h =self.addTwoNumbersSecondTimes10(h,  self.multiply(n1, n2.val))
            tmp = ListNode(0)
            tmp.next = h
            h = tmp
        return h

    def reverse(self, head):  #如果不能reverse。用stack就是一样的效果
        if not head: return
        dummy= ListNode(0); dummy.next=  head
        pre, last, cur = dummy, head, head.next
        while cur:  #last一直是最后一个。 不变。
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next   #四层的封闭连环
        return dummy.next

    def addTwoNumbersSecondTimes10(self, l1, l2):
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        tmp = ListNode(0)
        tmp.next = l2
        l2 = tmp    #第二个数乘以10

        dummy = ListNode(0)
        carry, cur = 0, dummy
        while l1 and l2:
            sum = l1.val+l2.val+carry
            carry = sum/10
            cur.next = ListNode(sum%10)
            l1, l2, cur = l1.next, l2.next, cur.next
        while l1:
            sum = l1.val + carry
            carry = sum/10
            cur.next = ListNode(sum%10)
            l1, cur = l1.next, cur.next
        while l2:
            sum = l2.val + carry
            carry = sum/10
            cur.next = ListNode(sum%10)
            l2, cur = l2.next, cur.next
        if carry==1: cur.next=ListNode(1)
        return self.reverse(dummy.next)
'''