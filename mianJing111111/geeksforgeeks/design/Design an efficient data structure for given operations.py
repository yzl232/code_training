# encoding=utf-8
'''


mutual data structure.
Heap的每个节点也存储pointer  到 双链表的指针。
双链表的每个节点也存储pointer到2个Heap的对应节点


A simple solution is to maintain a sorted array where smallest element is at first position and largest element is at last. The time complexity of findMin(), findMAx() and deleteMax() is O(1). But time complexities of deleteMin(), insert() and delete() will be O(n).





Design an efficient data structure for given operations

Design a Data Structure for the following operations. The data structure should be efficient enough to accommodate the operations according to their frequency.

1) findMin() : Returns the minimum item.
   Frequency: Most frequent

2) findMax() : Returns the maximum item.
    Frequency: Most frequent

3) deleteMin() : Delete the minimum item.
    Frequency: Moderate frequent

4) deleteMax() : Delete the maximum item.
    Frequency: Moderate frequent

5) Insert() : Inserts an item.
    Frequency: Least frequent

6) Delete() : Deletes an item.
    Frequency: Least frequent.




Design an efficient data structure for given operations

Design a Data Structure for the following operations. The data structure should be efficient enough to accommodate the operations according to their frequency.

1) findMin() : Returns the minimum item.
   Frequency: Most frequent

2) findMax() : Returns the maximum item.
    Frequency: Most frequent

3) deleteMin() : Delete the minimum item.
    Frequency: Moderate frequent

4) deleteMax() : Delete the maximum item.
    Frequency: Moderate frequent

5) Insert() : Inserts an item.
    Frequency: Least frequent

6) Delete() : Deletes an item.
    Frequency: Least frequent.

A simple solution is to maintain a sorted array where smallest element is at first position and largest element is at last. The time complexity of findMin(), findMAx() and deleteMax() is O(1). But time complexities of deleteMin(), insert() and delete() will be O(n).

Can we do the most frequent two operations in O(1) and other operations in O(Logn) time?.
The idea is to use two binary heaps (one max and one min heap). The main challenge is, while deleting an item, we need to delete from both min-heap and max-heap. So, we need some kind of mutual data structure. In the following design, we have used doubly linked list as a mutual data structure. The doubly linked list contains all input items and indexes of corresponding min and max heap nodes. The nodes of min and max heaps store addresses of nodes of doubly linked list. The root node of min heap stores the address of minimum item in doubly linked list. Similarly, root of max heap stores address of maximum item in doubly linked list. Following are the details of operations.

1) findMax(): We get the address of maximum value node from root of Max Heap. So this is a O(1) operation.

1) findMin(): We get the address of minimum value node from root of Min Heap. So this is a O(1) operation.

3) deleteMin(): We get the address of minimum value node from root of Min Heap. We use this address to find the node in doubly linked list. From the doubly linked list, we get node of Max Heap. We delete node from all three. We can delete a node from doubly linked list in O(1) time. delete() operations for max and min heaps take O(Logn) time.

4) deleteMax(): is similar to deleteMin()

5) Insert() We always insert at the beginning of linked list in O(1) time. Inserting the address in Max and Min Heaps take O(Logn) time. So overall complexity is O(Logn)

6) Delete() We first search the item in Linked List. Once the item is found in O(n) time, we delete it from linked list. Then using the indexes stored in linked list, we delete it from Min Heap and Max Heaps in O(Logn) time. So overall complexity of this operation is O(n). The Delete operation can be optimized to O(Logn) by using a balanced binary search tree instead of doubly linked list as a mutual data structure. Use of balanced binary search will not effect time complexity of other operations as it will act as a mutual data structure like doubly Linked List.

双链表优点在于插入删除都是O(1).    查找依然是O(n)
heap优点在于findMax, findMin都是O(1)。非常好。
删除max, min都是O(logn)
heap的每个node也存储pointer双链表的node

本来只用堆就好。但是删除要2个heap同时删除。 对于第二个堆。搜索最小值又要O(n) 因为heap得sibling之间没有关系。 只保证了parent更大而已
 deleteMin(), deleteMax()都要同时操作2个heap


 Delete()达到O(logn)要用bst
'''