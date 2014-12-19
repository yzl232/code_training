# encoding=utf-8
'''
Write a program to implement Double Linked List from Stack with min. complexity.
'''


'''
a double linked list should have these operation
go_pre
go_next
insert
delete
so we can use two stack to simulate a double linked list
stack1 store the data before the pointer now ,stack2 store the data after the pointer.
insert : push this element to s1
delete: pop element from s1
go_pre operation we can pop the top element from s1, and push to s2.
go_next : pop the element from s2 and push to s1.
this is the basic solution every operation is O(1)
these is some specific part need to be pay attention to.
'''



'''
Imagine all items are organized into two stacks, draw them facing each other where face is where you put and peek:

1,2,3,4-><-5,6,7,8

now you can move 4 to 5:

1,2,3-><-4,5,6,7,8

and 3 to 4:

1,2-><-3,4,5,6,7,8

and you can go backwards
'''