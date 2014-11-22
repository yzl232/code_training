class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
            
    def delete(self, node):
        if node.prev:     node.prev.next = node.next
        else:       self.head = node.next
        if node.next:         node.next.prev = node.prev
        else:        self.tail = node.prev

class LRUCache:
    def __init__(self, capacity):
        self.cache = LinkedList()
        self.d = {}
        self.capacity = capacity
        
    def _insert(self, key, val):
        node = ListNode(key, val)
        self.cache.insert(node)
        self.d[key] = node

    def get(self, key):
        if key in self.d:
            val = self.d[key].val
            self.cache.delete(self.d[key])
            self._insert(key, val)
            return val
        return -1

    def set(self, key, val):
        if key in self.d:
            self.cache.delete(self.d[key])
        elif len(self.d) == self.capacity:
            del self.d[self.cache.head.key]
            self.cache.delete(self.cache.head)
        self._insert(key, val)





        self.printList()

        print self.d.keys()

    def printList(self):
        node = self.cache.head
        s = ''
        while node:
            s+=str( node.key)+' '
            node = node.next
        print s
a = LRUCache(4)
a.set(2, 5)

a.set(10,13);a.set(3,17);a.set(6,11);a.set(10,5);a.set(9,10);a.get(13);a.set(2,19);a.get(2);a.get(3);
a.set(5,25);a.get(8);a.set(9,22);a.set(5,5);a.set(1,30);
a.get(7);a.get(5);a.get(8);a.get(9);a.set(4,30);a.set(9,3);a.get(9);a.get(10);a.get(10);a.set(6,14);a.set(3,1);a.get(3);a.set(10,11);a.get(8);a.set(2,14);a.get(1);a.get(5);a.get(4);a.set(11,4);a.set(12,24);a.set(5,18);a.get(13);a.set(7,23);a.get(8);a.get(12);a.set(3,27);a.set(2,12);a.get(5);a.set(2,9);a.set(13,4);a.set(8,18);a.set(1,7);a.get(6);a.set(9,29);a.set(8,21);a.get(5);a.set(6,30);a.set(1,12);a.get(10);a.set(4,15);a.set(7,22);a.set(11,26);a.set(8,17);a.set(9,29);a.get(5);a.set(3,4);a.set(11,30);a.get(12);a.set(4,29);a.get(3);a.get(9);a.get(6);a.set(3,4);a.get(1);a.get(10);a.set(3,29);a.set(10,28);a.set(1,20);a.set(11,13);a.get(3);a.set(3,12);a.set(3,8);a.set(10,9);a.set(3,26);a.get(8);a.get(7);a.get(5);a.set(13,17);a.set(2,27);a.set(11,15);a.get(12);a.set(9,19);a.set(2,15);a.set(3,16);a.get(1);a.set(12,17);a.set(9,1);a.set(6,19);a.get(4);a.get(5);a.get(5);a.set(8,1);a.set(11,7);a.set(5,2);a.set(9,28);a.get(1);a.set(2,2);a.set(7,4);a.set(4,22);a.set(7,24);a.set(9,26);a.set(13,28);a.set(11,26)