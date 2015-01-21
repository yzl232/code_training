# encoding=utf-8
'''
Given a Doubly Linked List which has data members sorted in ascending order. Construct a Balanced Binary Search Tree which has same data members as the given Doubly Linked List. The tree must be constructed in-place (No new node should be allocated for tree conversion)

Examples:

Input:  Doubly Linked List 1 <--> 2 <--> 3
Output: A Balanced BST
     2
   /  \
  1    3


Input: Doubly Linked List 1 <--> 2 <-->3 <--> 4 <-->5 <--> 6 <--> 7
Output: A Balanced BST
        4
      /   \
     2     6
   /  \   / \
  1   3  4   7

Input: Doubly Linked List 1 <--> 2 <--> 3 <--> 4
Output: A Balanced BST
      3
    /  \
   2    4
 /
1

Input:  Doubly Linked List 1 <--> 2 <--> 3 <--> 4 <--> 5 <--> 6
Output: A Balanced BST
      4
    /   \
   2     6
 /  \   /
1   3  5


基本上和leetcode上面的single linked list一样,
区别：
就是next改上了right。  prev变成left
另外不用新建node。 修改本身的node
'''


class Solution:
    def sortedListToBST(self, head):
        cur, cnt = head, 0
        while cur != None:
            cur, cnt = cur.right, cnt + 1
        self.h = head
        return self.help(0, cnt - 1)

    def help(self, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        left = self.help(start, mid - 1)  #最左边的left必然是None。  start 与 mid相等
        root = self.h    #与single list的不同
        root.left = left
        self.h = self.h.right
        root.right = self.help(mid + 1, end)
        return root