# encoding=utf-8
'''
find common elements in both


暴力法。 遍历 。存到hashmap.
Time O(n) ... Space O(n)


如果要space O(1)    先flatten BST to linkedlist(这个也不用额外开辟新的list内存)，然后你比较两个list的相交部分





InOrder traversing both the trees iteratively and checking for any common elements
Time O(n) ... Space O(log n)

高度为logN



Convert both trees to doubly linked list. O(n) space. And then find the intersection of these two linked lists. Much less space.

O(1) spae



http://www.careercup.com/question?id=14581972
'''
