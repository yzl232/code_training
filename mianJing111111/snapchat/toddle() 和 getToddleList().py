'''
一面国人小哥，人非常好。题目是面经里提过的 toddle() 和 getToddleList()，具体可以看这个帖子: 

http://www.1point3acres.com/bbs/thread-160016-1-1.html

用双链表解决应该是最好的。


刚面完电面。两道题。1. Design
// snapchatter send-list
// toggle(string username)
// getSelectedLlist() . 
// t: a getsl: a.  
// t: a b c getSl: a b c.  
// t: a b a c getSl: b c



比如 toddle(a), getList 返回 a；
再 toddle(b), getList 返回 a b;
再 toddle(c), getList 返回 a b c；
再 toddle(b)，getList 返回 a c
再 toddle(c)，getList 返回 a

包括了delete。   似乎用LRU Cache

 Design题我给的设计，用了doublelinkedlist，确保了toggle时的时间复杂度为O(1)
 
  同意，感觉就是doubleLinkedList + HashMap
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class LinkedList:
    def __init__(self):
        self.head =self.tail = None

    def insert(self, node):
        if not self.tail:     self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
        self.head = node

    def delete(self, node):
        if node.prev:     node.prev.next = node.next
        else:       self.head = node.next
        if node.next:         node.next.prev = node.prev
        else:        self.tail = node.prev

class LRUCache:
    def __init__(self, capacity):
        self.cache = LinkedList()
        self.d = {}
        self.curSelected = set()

    def toggle(self, s):
        if s not in self.d: 
            self._insert(s, s)
            self.curSelected.add(s)
        else:
            self.cache.delete(self.d[s])
            del self.d[s]
            self.curSelected.remove(s)
    def getList(self):
        return list(self.curSelected)

    def _insert(self, key, val):
        node = ListNode(key, val)
        self.cache.insert(node)
        self.d[key] = node