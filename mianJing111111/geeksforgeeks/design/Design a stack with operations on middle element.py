# encoding=utf-8
'''

Design a stack with operations on middle element

How to implement a stack which will support following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
Push and pop are standard stack operations.
难点在于deleteMiddle()

The important question is, whether to use a linked list or array for implementation of stack?

Please note that, we need to find and delete middle element. Deleting an element from middle is not O(1) for array. Also, we may need to move the middle pointer up when we push an element and move down when we pop(). In singly linked list, moving middle pointer in both directions is not possible.

The idea is to use Doubly Linked List (DLL). We can delete middle element in O(1) time by maintaining mid pointer. We can move mid pointer in both directions using previous and next pointers.

Following is C implementation of push(), pop() and findMiddle() operations. Implementation of deleteMiddle() is left as an exercise. If there are even elements in stack, findMiddle() returns the first middle element. For example, if stack contains {1, 2, 3, 4}, then findMiddle() would return 2.


就是用双链表和stack.
stack存储pointer to  双链表。  (把node 存进去)。
#middle pointer的的移动
#用一个self.cnt。 push的时候， 如果self.cnt==2,  middle后移， 并且self.cnt=0。

'''




# hasttable  优势： find 是O(1)
#  linkedlist优势： del, insert  O(1)
