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
    head = None
    def sortedListToBST(self, head):
        current, length = head, 0
        while current != None:
            current, length = current.right, length + 1
        self.head = head
        return self.sortedRecur(0, length - 1)

    def sortedRecur(self, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        left = self.sortedRecur(start, mid - 1)  #最左边的left必然是None。  start 与 mid相等
        root = self.head    #与single list的不同
        root.left = left
        self.head = self.head.right
        root.right = self.sortedRecur(mid + 1, end)
        return root