# encoding=utf-8
'''
 If we use extended approach discussed in the same post, we need to go through the count array every time first non-repeating element is queried. We can find the first non-repeating character from stream at any moment without traversing any array.



The idea is to use a DLL (Doubly Linked List) to efficiently get the first non-repeating character from a stream. The DLL contains all non-repeating characters in order, i.e., the head of DLL contains first non-repeating character, the second node contains the second non-repeating and so on.


hashtable + double linkedlist   艹。我的想法是正确的。

伪代码是这样：

 d[key] = (cnt, pointerToNode)

双链表只保存出现了一次的东东。

if a not in d:
    node = Node(a)
    doublLinkedList.addNodeToTail()
    d[key] = (cnt, node)
else:
    node = d[key][1]
    doubleLinkedList.remove()

'''


