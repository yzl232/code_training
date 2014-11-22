# encoding=utf-8
'''
http://openmymind.net/High-Concurrency-LRU-Caching/

'''

import threading
mylock = threading.RLock()   #Allocate a lock
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
        if self.tail is None:
            self.tail = node
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
        self.capacity = capacity

    def _insert(self, key, val):
        node = ListNode(key, val)
        self.cache.insert(node)
        self.d[key] = node

    def get(self, key):
        mylock.acquire()   #运行前放mylock.acquire()
        if key in self.d:
            val = self.d[key].val
            self.cache.delete(self.d[key])
            self._insert(key, val)
            mylock.release()  #运行后放mylock.release()
            return val
        mylock.release()#运行后放mylock.release()
        return -1

    def set(self, key, val):
        mylock.acquire()   #运行前放mylock.acquire()
        if key in self.d:
            self.cache.delete(self.d[key])
        elif len(self.d) == self.capacity:
            del self.d[self.cache.tail.key] #注意这 里的先后顺序。。。先DEL然后再removelast#######################
            self.cache.delete(self.cache.tail)
        self._insert(key, val)
        mylock.release() #运行后放mylock.release()